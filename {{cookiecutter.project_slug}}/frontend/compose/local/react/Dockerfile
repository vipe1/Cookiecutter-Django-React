FROM node:14

# Set the working directory
WORKDIR /app

# Expose the port 3000
EXPOSE 3000
# Set default container run command
CMD npm start

# Install app dependencies
COPY package.json /app
RUN npm cache clear --force
RUN npm install --legacy-peer-deps
RUN mkdir -p node_modules/.cache && chmod -R 777 node_modules/.cache