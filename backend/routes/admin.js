import express from "express";
import jwt from "jsonwebtoken";
import Student from "../models/Student.js";

const router = express.Router();

// Middleware to verify Admin JWT
const verifyAdmin = (req, res, next) => {
  const token = req.headers.authorization?.split(" ")[1];
  if (!token) return res.status(401).json({ success: false, message: "No token provided." });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    if (decoded.role !== "admin") {
      return res.status(403).json({ success: false, message: "Access denied. Admins only." });
    }
    next();
  } catch (error) {
    return res.status(401).json({ success: false, message: "Invalid or expired token." });
  }
};

// ─── ADMIN LOGIN ───────────────────────────────────────────────
router.post("/login", (req, res) => {
  try {
    const { username, password } = req.body;

    // Check credentials against .env
    const envUser = process.env.ADMIN_USERNAME;
    const envPass = process.env.ADMIN_PASSWORD;

    if (username === envUser && password === envPass) {
      // Generate Admin JWT
      const token = jwt.sign(
        { role: "admin", username },
        process.env.JWT_SECRET,
        { expiresIn: "1d" }
      );

      return res.status(200).json({
        success: true,
        message: "Admin login successful.",
        token,
      });
    }

    res.status(401).json({ success: false, message: "Invalid admin credentials." });
  } catch (error) {
    console.error("Admin Login Error:", error);
    res.status(500).json({ success: false, message: "Server error." });
  }
});

// ─── GET ALL USERS (STUDENTS) ──────────────────────────────────
router.get("/users", verifyAdmin, async (req, res) => {
  try {
    const users = await Student.find({}, "-password").sort({ created_at: -1 }); // exclude password field
    res.status(200).json({ success: true, users });
  } catch (error) {
    console.error("Get Users Error:", error);
    res.status(500).json({ success: false, message: "Failed to fetch users." });
  }
});

// ─── DELETE USER by ID ─────────────────────────────────────────
router.delete("/users/:id", verifyAdmin, async (req, res) => {
  try {
    const { id } = req.params;
    const deletedUser = await Student.findByIdAndDelete(id);
    
    if (!deletedUser) {
      return res.status(404).json({ success: false, message: "User not found." });
    }

    res.status(200).json({ success: true, message: "User safely deleted from the system." });
  } catch (error) {
    console.error("Delete User Error:", error);
    res.status(500).json({ success: false, message: "Failed to delete user." });
  }
});

export default router;
