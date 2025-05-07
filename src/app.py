from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(dict(request.json))
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete:", position)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['PUT'])
def update_todo(position):
    if position >= len(todos):
        return jsonify({"error": "Index out of range"}), 404
    
    updated_task = request.json
    todos[position] = updated_task
    print("Updated task at position:", position)
    return jsonify(todos)




















if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

