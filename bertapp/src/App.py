from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/checkin/<projectId>/<int:qty>', methods=['GET'])
def checkIn_hardware(projectId, qty):
    # For now, we're just returning the projectId and quantity.
    # In the full implementation, you'd interact with the database here.
    return jsonify({"message": f"{qty} hardware checked in", "projectId": projectId, "quantity": qty})

@app.route('/checkout/<projectId>/<int:qty>', methods=['GET'])
def checkOut_hardware(projectId, qty):
    # Similar to checkIn_hardware, this is a stub implementation.
    return jsonify({"message": f"{qty} hardware checked out", "projectId": projectId, "quantity": qty})

@app.route('/join/<projectId>', methods=['GET'])
def joinProject(projectId):
    # A stub implementation, would involve database checks in a full version.
    return jsonify({"message": f"Joined {projectId}", "projectId": projectId})

@app.route('/leave/<projectId>', methods=['GET'])
def leaveProject(projectId):
    # Stub implementation, actual version would involve more checks.
    return jsonify({"message": f"Left {projectId}", "projectId": projectId})

if __name__ == '__main__':
    app.run(debug=True)
