from flask  import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
import json

app = Flask(__name__)
CORS(app)
api = Api(app)

class Predict(Resource):
    def post(self):
        image = request.files.get('image')
        
        return {'message': 'Image received'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')