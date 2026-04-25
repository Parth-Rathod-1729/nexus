import express from 'express';
import multer from 'multer';
import { generatePipeline, getPipelineStatus } from '../controllers/pipelineController.js';

const router = express.Router();

// Memory store temporarily; pdfExtractor will immediately parse the buffer.
const upload = multer({ storage: multer.memoryStorage() });

router.post('/generate', upload.single('document'), generatePipeline);
router.get('/status/:jobId', getPipelineStatus);

export default router;
