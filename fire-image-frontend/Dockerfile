FROM node:16

WORKDIR /frontend

COPY package*.json ./

RUN npm install

COPY . .

ARG NEXT_PUBLIC_BACKEND_SERVICE_IP

ENV NEXT_PUBLIC_BACKEND_SERVICE_IP=$NEXT_PUBLIC_BACKEND_SERVICE_IP

RUN npm run build

ENV NODE_ENV production

EXPOSE 3000

CMD ["npm", "start"]
