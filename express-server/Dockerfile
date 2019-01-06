# Create image based on the official Node 6 image from the dockerhub
FROM node:6

WORKDIR /usr/src/app

# Copy dependency definitions
COPY package.json /usr/src/app
# Install dependecies
RUN npm install

# Get all the code needed to run the app
COPY . /usr/src/app

EXPOSE 3000

# Serve the app
CMD ["npm", "start"]
