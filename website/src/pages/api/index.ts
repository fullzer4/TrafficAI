import { NextApiHandler } from 'next';
import graphqlHandler from './graphql';

const handler: NextApiHandler = (req, res) => {
  if (req.method === 'GET') {
    res.end('API is running');
  } else {
    return graphqlHandler(req, res);
  }
};

export default handler;