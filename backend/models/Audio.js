import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

const audioSchema = new mongoose.Schema({
  audio_id: {
    type: String,
    default: uuidv4,
    unique: true,
  },
  scene_id: {
    type: String,
    ref: "Scene",
    required: true,
  },
  audio_url: {
    type: String,
    required: true,
  },
  duration: {
    type: Number,
  },
  voice_type: {
    type: String,
  },
});

const Audio = mongoose.model("Audio", audioSchema);
export default Audio;
