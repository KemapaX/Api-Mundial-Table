from flask import Flask, jsonify
import controller as apis

server = Flask("Api-tables")

#this 
@server.get('/')
def api():
    return jsonify({'messege': "Welcome to Api-Tables"})

@server.get('/show')
def show_table():
    return apis.show() 

if __name__ == '__main__':
    server.run(debug=True)