import subprocess
import sys
import json
import os
import shutil

def run_manim(file_path, scene_name, job_id):
    # Resolve absolute paths relative to this script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.abspath(os.path.join(script_dir, "..", "backend"))

    # Dynamically locate FFmpeg in the backend node_modules
    ffmpeg_dir = os.path.join(backend_dir, "node_modules", "@ffmpeg-installer", "win32-x64")
    if os.path.exists(ffmpeg_dir):
        os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ["PATH"]

    # Absolute path where Manim will write its output
    media_dir = os.path.abspath(os.path.join(backend_dir, "temp", "videos", job_id, scene_name))

    # Final destination for the renamed mp4 (flat structure expected by Node.js)
    final_dir = os.path.abspath(os.path.join(backend_dir, "temp", "videos", job_id))
    final_path = os.path.join(final_dir, f"{scene_name.lower()}.mp4")
    os.makedirs(final_dir, exist_ok=True)

    # Use sys.executable -m manim for robustness
    # -pql = preview, low quality (fast). Remove -p on servers (no display)
    command = [
        sys.executable, "-m", "manim",
        "-ql",               # low quality, no preview popup
        "--disable_caching",
        file_path, scene_name,
        "--media_dir", media_dir
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=300,  # 5 min hard timeout
        )

        # Walk the entire media_dir for any .mp4 file
        video_found = False
        if os.path.exists(media_dir):
            for root, dirs, files in os.walk(media_dir):
                for f in files:
                    if f.lower().endswith(".mp4"):
                        source_path = os.path.join(root, f)
                        shutil.copy2(source_path, final_path)
                        video_found = True
                        break
                if video_found:
                    break

        if video_found:
            print(json.dumps({"success": True, "path": final_path}))
        else:
            stderr_snippet = (result.stderr or result.stdout or "No output")[-1500:]
            print(json.dumps({
                "success": False,
                "error": f"No MP4 produced by Manim. stderr: {stderr_snippet}"
            }))

    except subprocess.TimeoutExpired:
        print(json.dumps({"success": False, "error": "Manim execution timed out (300s)."}))
    except subprocess.CalledProcessError as e:
        print(json.dumps({"success": False, "error": e.stderr[-1500:] if e.stderr else str(e)}))
    except Exception as e:
        print(json.dumps({"success": False, "error": str(e)}))


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(json.dumps({
            "success": False,
            "error": "Missing arguments. Usage: python runner.py <file.py> <SceneName> <jobId>"
        }))
        sys.exit(1)

    file_py = sys.argv[1]
    scene_name = sys.argv[2]
    job_id = sys.argv[3]

    run_manim(file_py, scene_name, job_id)
