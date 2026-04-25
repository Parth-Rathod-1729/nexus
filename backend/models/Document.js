import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

const documentSchema = new mongoose.Schema({
  doc_id: {
    type: String,
    default: uuidv4,
    unique: true,
  },
  student_id: {
    type: String,
    ref: "Student",
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  file_url: {
    type: String,
    required: true,
  },
  uploaded_at: {
    type: Date,
    default: Date.now,
  },
  status: {
    type: String,
    default: "pending",
  },
});

const Document = mongoose.model("Document", documentSchema);
export default Document;
