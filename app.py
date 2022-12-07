from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import controller as apis

server = Flask("Api-tables")
CORS(server)


@cross_origin
@server.get('/')
def api():
    return jsonify({'messege': "Welcome to Api-Tables"})


@cross_origin
@server.get('/show')
def show_table():
    password = request.args.get('pass')
    return apis.show(password) 


if __name__ == '__main__':
    server.run(debug=True)