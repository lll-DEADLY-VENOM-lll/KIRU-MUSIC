FROM python:3.10-slim-buster

# 1. System Dependencies install karein
RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    curl \
    git \
    gnupg \
    ffmpeg \
    build-essential \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2. Node.js 20 (LTS) install karein (Official Method)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

# 3. Path Fix (Yeh sabse zaroori hai)
# Agar node install ho gaya hai phir bhi nahi mil raha, toh yeh command usse fix kar degi
RUN ln -sf /usr/bin/node /usr/local/bin/node && \
    ln -sf /usr/bin/npm /usr/local/bin/npm

# 4. App directory setup
WORKDIR /app
COPY . .

# 5. Python packages install karein
RUN pip3 install --no-cache-dir -U -r requirements.txt

# 6. Start command
CMD ["bash", "start"]
