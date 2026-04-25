import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

const pipelineLogSchema = new mongoose.Schema({
  log_id: {
    type: String,
    default: uuidv4,
    unique: true,
  },
  project_id: {
    type: String,
    ref: "Project",
    required: true,
  },
  step_name: {
    type: String,
    required: true,
  },
  status: {
    type: String,
    required: true,
  },
  timestamp: {
    type: Date,
    default: Date.now,
  },
  message: {
    type: String,
  },
});

const PipelineLog = mongoose.model("PipelineLog", pipelineLogSchema);
export default PipelineLog;
