FROM node:slim

WORKDIR /node/app
COPY ./node-files/ ./
RUN npm install lite-server

CMD ["npm", "run", "lite"]