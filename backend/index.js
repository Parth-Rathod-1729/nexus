import "dotenv/config";
import express from "express";
import mongoose from "mongoose";
import cors from "cors";

// Import all models (registers collections in MongoDB)
import Student from "./models/Student.js";
import Document from "./models/Document.js";
import DocumentChunk from "./models/DocumentChunk.js";
import Project from "./models/Project.js";
import Scene from "./models/Scene.js";
import ManimCode from "./models/ManimCode.js";
import Audio from "./models/Audio.js";
import Video from "./models/Video.js";
import FinalVideo from "./models/FinalVideo.js";
import PipelineLog from "./models/PipelineLog.js";
import Admin from "./models/Admin.js";
import Agent from "./models/Agent.js";

// Route imports
import authRoutes from "./routes/auth.js";
import adminRoutes from "./routes/admin.js";
import pipelineRoutes from "./routes/pipeline.js";
import questionRoutes from "./routes/question.js";




const app = express();
const PORT = process.env.PORT || 4000;

// Middleware
app.use(cors());
app.use(express.json());

// API Routes
app.use("/api/auth", authRoutes);
app.use("/api/admin", adminRoutes);
app.use("/api/pipeline", pipelineRoutes);
app.use("/api/questions", questionRoutes);


// Serve videos statically
app.use("/videos", express.static("temp/videos"));

// MongoDB Connection
const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_DB_LINK);
    console.log("MongoDB connected successfully");
  } catch (error) {
    console.error("MongoDB connection failed:", error.message);
    process.exit(1);
  }
};

// Test route
app.get("/", (req, res) => {
  res.json({ message: "Nexus API is running " });
});

// Connect to DB and start server
connectDB().then(() => {
  app.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on port ${PORT}`);
  });
});