from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/checkin/<projectId>/<int:qty>', methods=['GET'])
def checkIn_hardware(projectId, qty):
    return jsonify({"message": f"{qty} hardware checked in", "projectId": projectId, "quantity": qty})

@app.route('/checkout/<projectId>/<int:qty>', methods=['GET'])
def checkOut_hardware(projectId, qty):
    return jsonify({"message": f"{qty} hardware checked out", "projectId": projectId, "quantity": qty})

@app.route('/join/<projectId>', methods=['GET'])
def joinProject(projectId):
    return jsonify({"message": f"Joined {projectId}", "projectId": projectId})

@app.route('/leave/<projectId>', methods=['GET'])
def leaveProject(projectId):
    return jsonify({"message": f"Left {projectId}", "projectId": projectId})

@app.route('/', methods=['GET'])
def home():
    return "Backend server is running!"

if __name__ == '__main__':
    app.run(debug=True)
