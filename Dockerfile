FROM node:20-bookworm

# Install Python and Manim system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    ffmpeg \
    libcairo2-dev \
    libpango1.0-dev \
    pkg-config \
    texlive \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-latex-recommended \
    texlive-science \
    tipa \
    && rm -rf /var/lib/apt/lists/*

# Set up virtual environment and install Python packages
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Install Python packages first for caching
COPY python-service/requirements.txt ./python-service/
RUN pip install --no-cache-dir -r python-service/requirements.txt

# Install Node dependencies
COPY backend/package*.json ./backend/
RUN cd backend && npm install

# Copy source code
COPY python-service/ ./python-service/
COPY backend/ ./backend/

# The API runs on 4000 by default, but Railway injects PORT
ENV PORT=4000
EXPOSE 4000

# Start backend from within the backend directory
WORKDIR /app/backend
CMD ["node", "index.js"]
