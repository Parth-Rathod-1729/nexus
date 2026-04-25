import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

const documentChunkSchema = new mongoose.Schema({
  chunk_id: {
    type: String,
    default: uuidv4,
    unique: true,
  },
  doc_id: {
    type: String,
    ref: "Document",
    required: true,
  },
  content: {
    type: String,
    required: true,
  },
  embedding: {
    type: String,
  },
  page_no: {
    type: Number,
  },
  created_at: {
    type: Date,
    default: Date.now,
  },
});

const DocumentChunk = mongoose.model("DocumentChunk", documentChunkSchema);
export default DocumentChunk;
