import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

const sceneSchema = new mongoose.Schema({
  scene_id: {
    type: String,
    default: uuidv4,
    unique: true,
  },
  project_id: {
    type: String,
    ref: "Project",
    required: true,
  },
  scene_order: {
    type: Number,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
  },
  script: {
    type: String,
  },
  visual_context: {
    type: String,
  },
  audio_context: {
    type: String,
  },
});

const Scene = mongoose.model("Scene", sceneSchema);
export default Scene;
