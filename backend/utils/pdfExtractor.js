import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const pdfParse = require('pdf-parse');
/**
 * Extracts text from a PDF buffer and limits to the given character count.
 * @param {Buffer} buffer - The uploaded PDF buffer
 * @param {number} maxChars - The maximum characters to return
 * @returns {Promise<string>} The extracted text
 */
export async function extractText(buffer, maxChars = 8000) {
    try {
        const data = await pdfParse(buffer);
        let text = data.text || '';
        // Clean up whitespace
        text = text.replace(/\s+/g, ' ').trim();
        // Limit to max chars
        return text.slice(0, maxChars);
    } catch (error) {
        throw new Error('Failed to extract text from PDF: ' + error.message);
    }
}
