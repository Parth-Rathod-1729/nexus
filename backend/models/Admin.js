import mongoose from "mongoose";

const adminSchema = new mongoose.Schema({
  admin_id: {
    type: String,
    required: true,
    unique: true,
  },
  name: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
    unique: true,
  },
  password: {
    type: String,
    required: true,
  },
  role: {
    type: String,
    default: "admin",
  },
  created_at: {
    type: Date,
    default: Date.now,
  },
});

const Admin = mongoose.model("Admin", adminSchema);
export default Admin;
