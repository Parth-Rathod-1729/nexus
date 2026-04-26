

import sys
import json
import os
from gtts import gTTS
from moviepy import VideoFileClip, AudioFileClip, concatenate_audioclips, ColorClip

def get_ffmpeg_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.abspath(os.path.join(script_dir, "..", "backend"))
    ffmpeg_dir = os.path.join(backend_dir, "node_modules", "@ffmpeg-installer", "win32-x64")
    if os.path.exists(ffmpeg_dir):
        return os.path.join(ffmpeg_dir, "ffmpeg.exe")
    return "ffmpeg"

def process_audio_video(video_path, narration_text, output_path, language='english'):
    # Use a unique temp audio file based on output path to avoid collisions
    temp_audio = output_path.replace(".mp4", f"_temp_{os.getpid()}.mp3")
    
    try:
        # 1. Generate TTS or Silence
        is_existing_file = narration_text.lower().endswith(".mp3") and os.path.exists(narration_text)
        
        if is_existing_file:
            # If it's already a path to an mp3 (from CAMB.AI), use it directly
            source_audio = narration_text
            temp_audio = None
        elif not narration_text.strip():
            # Create a 1-second silent mp3 if no narration
            temp_audio = output_path.replace(".mp4", f"_temp_{os.getpid()}.mp3")
            from moviepy import AudioArrayClip
            import numpy as np
            silence_arr = np.zeros((44100, 2))
            audio = AudioArrayClip(silence_arr, fps=44100)
            audio.write_audiofile(temp_audio, logger=None)
            source_audio = temp_audio
        else:
            temp_audio = output_path.replace(".mp4", f"_temp_{os.getpid()}.mp3")
            tld = 'com'
            if language == 'hinglish':
                lang_code = 'en'
                tld = 'co.in'
            elif language == 'hindi':
                lang_code = 'hi'
                tld = 'co.in'
            else:
                lang_code = 'en'
            
            tts = gTTS(text=narration_text, lang=lang_code, tld=tld)
            tts.save(temp_audio)
            source_audio = temp_audio
        
        # 2. Load video and audio
        video = VideoFileClip(video_path)
        audio = AudioFileClip(source_audio)
        
        # 3. Handle duration mismatch
        v_dur = video.duration
        a_dur = audio.duration
        
        # We prioritize the narration. If video is too short, we loop it or pad it.
        # But for Manim, usually we want the video to match the narration.
        # If narration is much longer, we might have a problem.
        # For now, let's stick to matching the longer of the two, but capping it.
        
        if a_dur > v_dur:
            # Video is shorter than narration. 
            # Pad the video with its last frame to match audio duration.
            last_frame_img = video.get_frame(v_dur - 0.1)
            from moviepy import ImageClip, concatenate_videoclips
            freeze_dur = a_dur - v_dur
            freeze_clip = ImageClip(last_frame_img).with_duration(freeze_dur).with_fps(video.fps or 24)
            final_video = concatenate_videoclips([video, freeze_clip])
            final_audio = audio
        else:
            # Video is longer than narration. Pad audio with silence.
            silence_dur = v_dur - a_dur
            if silence_dur > 0:
                # Create silence by scaling volume of a clip
                silence = audio.with_volume_scaled(0).with_duration(silence_dur)
                final_audio = concatenate_audioclips([audio, silence])
            else:
                final_audio = audio
            final_video = video
        
        # 4. Set audio to video
        final_video = final_video.with_audio(final_audio)
        
        # 5. Write output
        # Use a unique temp_audiofile to avoid collisions
        temp_m4a = output_path.replace(".mp4", f"_temp_{os.getpid()}.m4a")
        final_video.write_videofile(
            output_path, 
            codec="libx264", 
            audio_codec="aac", 
            temp_audiofile=temp_m4a, 
            remove_temp=True, 
            fps=video.fps or 24,
            logger=None,
            threads=2
        )
        
        # Cleanup
        video.close()
        audio.close()
        if temp_audio and os.path.exists(temp_audio):
            os.remove(temp_audio)
        if os.path.exists(temp_m4a):
            os.remove(temp_m4a)
            
        return {"success": True, "path": output_path}
    except Exception as e:
        # Cleanup on error
        if 'video' in locals(): video.close()
        if 'audio' in locals(): audio.close()
        if 'temp_audio' in locals() and temp_audio and os.path.exists(temp_audio): os.remove(temp_audio)
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(json.dumps({"success": False, "error": "Usage: audio_handler.py <video_path> <narration_text> <output_path>"}))
        sys.exit(1)
        
    v_path = sys.argv[1]
    text = sys.argv[2]
    out_path = sys.argv[3]
    lang = sys.argv[4] if len(sys.argv) > 4 else 'english'
    
    # Configure moviepy to use the local ffmpeg if found
    ffmpeg_exe = get_ffmpeg_path()
    os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_exe

    result = process_audio_video(v_path, text, out_path, lang)
    print(json.dumps(result))
