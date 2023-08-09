# Use an official Node.js runtime as the base image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the entire project to the container
COPY . .

# Build the Vite project
RUN npm run build

# Expose the port that your Vite app runs on
EXPOSE 3000

# Run the Vite app when the container starts
CMD ["npm", "run", "dev"]
