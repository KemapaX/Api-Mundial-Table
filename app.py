from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import controller as apis

server = Flask("Api-tables")
CORS(server)


@cross_origin
@server.get('/')
def api():
    return jsonify({'messege': "Welcome to Api-Tables"})


@cross_origin
@server.get('/show/<password>')
def show_table(password):
    return apis.show(password) 

if __name__ == '__main__':
    server.run(debug=True)