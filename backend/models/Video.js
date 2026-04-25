import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

const videoSchema = new mongoose.Schema({
  video_id: {
    type: String,
    default: uuidv4,
    unique: true,
  },
  scene_id: {
    type: String,
    ref: "Scene",
    required: true,
  },
  video_url: {
    type: String,
    required: true,
  },
  resolution: {
    type: String,
  },
  duration: {
    type: Number,
  },
});

const Video = mongoose.model("Video", videoSchema);
export default Video;
