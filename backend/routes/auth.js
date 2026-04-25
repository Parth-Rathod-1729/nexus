import express from "express";
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import { v4 as uuidv4 } from "uuid";
import Student from "../models/Student.js";

const router = express.Router();

// ─── REGISTER ───────────────────────────────────────────────
router.post("/register", async (req, res) => {
  try {
    const { name, email, password, institute_name } = req.body;

    // Validate required fields
    if (!name || !email || !password) {
      return res.status(400).json({ 
        success: false, 
        message: "Name, email, and password are required." 
      });
    }

    // Check if email already exists
    const existingStudent = await Student.findOne({ email: email.toLowerCase() });
    if (existingStudent) {
      return res.status(409).json({ 
        success: false, 
        message: "An account with this email already exists." 
      });
    }

    // Hash password
    const salt = await bcrypt.genSalt(12);
    const hashedPassword = await bcrypt.hash(password, salt);

    // Create student
    const student = new Student({
      student_id: uuidv4(),
      name,
      email: email.toLowerCase(),
      password: hashedPassword,
      institute_name: institute_name || "Not Specified",
    });

    await student.save();

    res.status(201).json({
      success: true,
      message: "Registration successful. You can now log in.",
    });
  } catch (error) {
    console.error("Register error:", error.message);
    res.status(500).json({ 
      success: false, 
      message: "Server error during registration." 
    });
  }
});

// ─── LOGIN ──────────────────────────────────────────────────
router.post("/login", async (req, res) => {
  try {
    const { email, password } = req.body;

    // Validate
    if (!email || !password) {
      return res.status(400).json({ 
        success: false, 
        message: "Email and password are required." 
      });
    }

    // Find student by email
    const student = await Student.findOne({ email: email.toLowerCase() });
    if (!student) {
      return res.status(401).json({ 
        success: false, 
        message: "Invalid email or password." 
      });
    }

    // Compare password
    const isMatch = await bcrypt.compare(password, student.password);
    if (!isMatch) {
      return res.status(401).json({ 
        success: false, 
        message: "Invalid email or password." 
      });
    }

    // Generate JWT
    const token = jwt.sign(
      { 
        id: student._id, 
        student_id: student.student_id, 
        email: student.email,
        name: student.name 
      },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRY || "1d" }
    );

    res.status(200).json({
      success: true,
      message: "Login successful.",
      token,
      user: {
        id: student._id,
        student_id: student.student_id,
        name: student.name,
        email: student.email,
        institute_name: student.institute_name,
      },
    });
  } catch (error) {
    console.error("Login error:", error.message);
    res.status(500).json({ 
      success: false, 
      message: "Server error during login." 
    });
  }
});

export default router;
