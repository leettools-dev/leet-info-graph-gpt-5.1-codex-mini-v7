FROM node:20-slim
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
CMD ["python", "-m", "http.server", "3000"]
