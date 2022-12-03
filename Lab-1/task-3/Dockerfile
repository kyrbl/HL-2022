FROM node:slim

WORKDIR /node/app
COPY ./node-files/ ./
RUN npm install

CMD ["npm", "run", "json"]