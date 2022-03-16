FROM node:14

# Set the working directory
WORKDIR /app

# Expose the port 3000
EXPOSE 3000
# Set default container run command
CMD npm serve -s -n build

# Install app dependencies
COPY package.json /app
RUN npm cache clear --force
RUN npm install --legacy-peer-deps
RUN npm install -g serve
RUN mkdir -p node_modules/.cache && chmod -R 777 node_modules/.cache

# Add rest of the client code
COPY . /app

# Build the code
RUN npm run build