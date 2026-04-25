import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

const manimCodeSchema = new mongoose.Schema({
  code_id: {
    type: String,
    default: uuidv4,
    unique: true,
  },
  scene_id: {
    type: String,
    ref: "Scene",
    required: true,
  },
  code: {
    type: String,
    required: true,
  },
  status: {
    type: String,
    default: "pending",
  },
  error_log: {
    type: String,
  },
});

const ManimCode = mongoose.model("ManimCode", manimCodeSchema);
export default ManimCode;
