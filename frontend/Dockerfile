  # Stage 1: Build React app
  FROM node:24-alpine as builder

  WORKDIR /app
  COPY package*.json ./
  RUN npm install
  COPY . .
  RUN npm run build 
  

  # Stage 2: Serve static files
  FROM nginx:alpine
  COPY --from=builder /app/dist /usr/share/nginx/html 
  COPY nginx.conf /etc/nginx/conf.d/default.conf
  EXPOSE 80
  CMD ["nginx", "-g", "daemon off;"]