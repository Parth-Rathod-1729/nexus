import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

const agentSchema = new mongoose.Schema({
  agent_id: {
    type: String,
    default: uuidv4,
    unique: true,
  },
  name: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    required: true,
  },
  description: {
    type: String,
  },
});

const Agent = mongoose.model("Agent", agentSchema);
export default Agent;
