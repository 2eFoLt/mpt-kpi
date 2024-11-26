FROM node:22-alpine AS build-stage

RUN apk add python3 g++ make py3-pip 

WORKDIR /app

COPY package.json /app/
RUN npm install --production

COPY . /app/
RUN npm run build

EXPOSE ${FRONTEND_PORT}

CMD ["npm", "run", "serve"]
