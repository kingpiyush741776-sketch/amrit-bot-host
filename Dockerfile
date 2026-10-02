FROM node:20-bookworm-slim

# 🔥 150 Bots Memory Optimizer (Single Process High-Density)
ENV PYTHONOPTIMIZE=2
ENV MALLOC_ARENA_MAX=2
ENV NODE_OPTIONS="--max-old-space-size=128"

RUN apt-get update && apt-get install -y python3 python3-pip unzip && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY amrit_mental_fullstack.zip .
RUN unzip -o amrit_mental_fullstack.zip
COPY patch.py .
RUN python3 patch.py
RUN pip3 install --no-cache-dir --break-system-packages python-telegram-bot==21.6 httpx aiohttp
RUN npm install --legacy-peer-deps
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
