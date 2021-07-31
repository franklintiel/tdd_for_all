FROM node:15.0.1-alpine3.10 as builder
WORKDIR /app
COPY . .
COPY .env.production.local .env.production.local
RUN yarn install
RUN yarn cache clean
RUN yarn build

FROM nginx:1.16.0-alpine
COPY --from=builder /app/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/site.conf /etc/nginx/conf.d
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]

