FROM node:6

WORKDIR /usr/src/app

# Copy dependency definitions
COPY package.json /usr/src/app
# Install dependecies
RUN npm install

# Get all the code needed to run the app
COPY . /usr/src/app

EXPOSE 4200

# Serve the app --> see package.json.
CMD ["npm", "start"]
