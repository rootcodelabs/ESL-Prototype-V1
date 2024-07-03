# Use  an official Node.js runtime as parent image
FROM node:17-alpine as build

# Set the working directory to /app
WORKDIR /app

# Copy dependency files
COPY package.json ./
COPY package-lock.json ./

# Install dependencies
RUN npm install

# Copy Application Code
COPY . ./

# Build the app for production
RUN npm run build

# Base Image for final stage
FROM nginx:alpine

# Copy the build output to replace the default nginx contents
COPY --from=build /app/build /usr/share/nginx/html

# Expose Port
EXPOSE 80

# Command to run nginx
CMD [ "nginx", "-g", "daemon off;" ]