FROM node:latest

WORKDIR /app/frontend

COPY package.json /app/frontend

RUN npm install --legacy-peer-deps
RUN mkdir -p node_modules/.cache && chmod -R 777 node_modules/.cache

# Add rest of the client code
COPY . /app/frontend

EXPOSE 3000

CMD npm start
