import { ApolloServer } from "apollo-server";

const server = new ApolloServer({

})

export const config = {
    api: {
        bodyparser: false,
    },
}

const startServer = server.start()

export default async function handler(req, res){
    await startServer;
    await server.createHandler({ path: "/api/graphql" })(req, res)
}