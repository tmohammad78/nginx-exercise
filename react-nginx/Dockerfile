FROM node:16 AS builder

ENV NODE_ENV=production

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

ENV NODE_PATH=/app/node_modules

COPY . /app/

RUN npm run build

FROM nginx:alpine

WORKDIR /usr/share/nginx/html

RUN rm -rf *

COPY --from=builder /app/build /usr/share/nginx/html/
COPY --from=builder /app/nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/nginx/error /usr/share/nginx/html

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]
