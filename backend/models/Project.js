import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

const projectSchema = new mongoose.Schema({
  project_id: {
    type: String,
    default: uuidv4,
    unique: true,
  },
  doc_id: {
    type: String,
    ref: "Document",
    required: true,
  },
  student_id: {
    type: String,
    ref: "Student",
    required: true,
  },
  topic: {
    type: String,
    required: true,
  },
  status: {
    type: String,
    default: "created",
  },
  created_at: {
    type: Date,
    default: Date.now,
  },
});

const Project = mongoose.model("Project", projectSchema);
export default Project;
