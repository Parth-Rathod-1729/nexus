import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

const finalVideoSchema = new mongoose.Schema({
  final_video_id: {
    type: String,
    default: uuidv4,
    unique: true,
  },
  project_id: {
    type: String,
    ref: "Project",
    required: true,
  },
  video_url: {
    type: String,
    required: true,
  },
  total_duration: {
    type: Number,
  },
  created_at: {
    type: Date,
    default: Date.now,
  },
});

const FinalVideo = mongoose.model("FinalVideo", finalVideoSchema);
export default FinalVideo;
