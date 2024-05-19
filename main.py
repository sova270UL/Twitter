from flask import Flask, jsonify, request
import json
from model.twit import Twit

twits = []

app = Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Twit):
            return {'body': obj.body, 'author': obj.author}
        else:
            return super().default(obj)
        
app.json_encoder = CustomJSONEncoder

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})

@app.route('/twit', methods=['POST'])
def create_twit():
    '''
    {"body": "Hello World", "author": "@sova270", "id": 1}
    создает новый твит
    '''
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'], twit_json['id'])
    twit.id = len(twits) + 1
    twits.append(twit)
    return jsonify({'status': 'success'})

@app.route('/twit', methods=['GET'])
def read_twit():
    ''' получение всех твитов '''
    return jsonify({'twits': [twit.__dict__ for twit in twits]})

@app.route('/twit/<int:twit_id>', methods=['GET'])
def read_twit_by_id(twit_id):
    ''' получение твита по id '''
    return jsonify({'twit': [twit.__dict__ for twit in twits if twit.id == twit_id]})

@app.route('/twit/<int:twit_id>', methods=['DELETE'])
def delete_twit_by_id(twit_id):
    ''' удаление твита по id '''
    twit = [twit for twit in twits if twit.id == twit_id]
    twits.remove(twit[0])
    return jsonify({'status': 'success'})
    
@app.route('/twit/<int:twit_id>', methods=['PUT'])
def update_twit(twit_id):
    ''' изменение твита по id '''
    twit_json = request.get_json()
    twit = [twit for twit in twits if twit.id == twit_id]
    twit[0].body = twit_json['body']
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)