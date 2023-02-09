FROM node:19-alpine

ENV NODE_ENV=production

RUN apk add --no-cache libc6-compat

WORKDIR /authApp

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

COPY nodemon.json tsconfig.json ./

COPY . .

CMD [ "yarn", "start" ]