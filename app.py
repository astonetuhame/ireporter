"""
app root of the api endpoints
"""

import re
from datetime import datetime
from flask import Flask, jsonify, request

APP = Flask(__name__)

TYPEOFRECORD = ['red-flag', 'intervention']
INCIDENT = [
    {
        "id": 0,
        "createdOn" : "24/11/2018",
        "createdBy" : 1,
        "type" : "red-flag",
        "location" : "30.789 0.178",
        "status" : "draft",
        "Images" : ["c.jpg", "d.jpg"],
        "Videos": ["d.mp4", "e.mp4"],
        "comment":"Government stole money"
    },
    {
        "id": 1,
        "createdOn" : "30/11/2018",
        "createdBy" : 4,
        "type" : "intervention",
        "location" : "30.789 0.178",
        "status" : "draft",
        "Images" : ["a.jpg", "b.jpg"],
        "Videos": ["a.mp4", "b.mp4"],
        "comment":"Government stole nssf"
        }]

def _get_red_flag(_id):
    return [incident for incident in INCIDENT if incident['id'] == _id]

@APP.route('/api/v1/red-flags', methods=['POST'])
def create_red_flag_record():
    """Function to create red-flag record"""
    incident_id = INCIDENT[-1].get("id") + 1
    created_by = request.json.get('createdBy')
    location = request.json.get('location')
    type_of_incident = request.json.get('type')
    images = request.json.get('Images')
    videos = request.json.get('Videos')
    comment = request.json.get('comment')

    if not (isinstance(images, list) or isinstance(videos, list)):
        return jsonify({'status': 400, 'error':'Image or Video should be a list'}), 400
    for i in images:
        if not isinstance(i, str):
            return jsonify({'status': 400, 'error':'Character strings needed for Images sequence'}), 400
        if len(i) == 0:
            return jsonify({'status': 400, 'error':'Image cannot be empty'}), 400
    for i in videos:
        if not isinstance(i, str):
            return jsonify({'status': 400, 'error':'Character strings needed for Videos sequence'}), 400
        if len(i) == 0:
            return jsonify({'status': 400, 'error':'Video cannot be empty'}), 400
    if not request.json or 'location' not in request.json or 'Images' not in request.json  or 'Videos' not in request.json or 'comment' not in request.json or 'createdBy' not in request.json:
        reply = jsonify({'error': 'BAD_REQUEST'}), 400
    elif not (isinstance(comment, str) or isinstance(type_of_incident, str) or isinstance(location, str)):
        reply = jsonify({'status': 400, 'error':'Please use character strings'}), 400
    elif re.search(r"\s", location) or re.search(r"\s", type_of_incident):
        reply = jsonify({'status': 400, 'error':'No whitespaces allowed'}), 400
    elif type_of_incident.lower() not in TYPEOFRECORD:
        reply = jsonify({'status': 400, 'error':'Input red-flag or intervention'}), 400
    elif not location or not comment:
        reply = jsonify({'status': 400, 'error':'Field should atleast contain a character'}), 400
    elif not isinstance(created_by, int):
        reply = jsonify({'status': 400, 'error':'Please use integer values'}), 400
    else:
        incident = {"id": incident_id, "createdOn": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "createBy": created_by, "type": type_of_incident, "status": "draft", "Images": images, "Videos": videos, "comment": comment, "location": location}
        INCIDENT.append(incident)
        reply = jsonify({'status': 201, "data":[{"id":incident['id'], "message": "Created red-flag record"}]}), 201
    return reply

@APP.route('/api/v1/red-flags', methods=['GET'])
def get_red_flags():
    """Function to get all red-flags"""
    return jsonify({'status': 200, 'data': INCIDENT}), 200

@APP.route('/api/v1/red-flags/<int:_id>', methods=['GET'])
def get_red_flag(_id):
    """Function to get specific red-flag"""
    red_flag = _get_red_flag(_id)
    if not red_flag:
        return jsonify({'status': 404, 'error': "Red-flag record not found"}), 404
    return jsonify({'status': 200, "data": red_flag})

@APP.route('/api/v1/red-flags/<int:_id>', methods=['DELETE'])
def delete_red_flag(_id):
    """Function to delete a red-flag"""
    incident = _get_red_flag(_id)
    if len(incident) == 0:
        return jsonify({'status': 404, 'error': "Red-flag record not found"}), 404
    INCIDENT.remove(incident[0])
    return jsonify({'status': 200, "data":[{"id": incident[0]['id'], "message": "red-flag record has been deleted"}]}), 200

@APP.route('/api/v1/red-flags/<int:_id>/location', methods=['PATCH'])
def update_red_flag_location(_id):
    """Function to edit location of a red-flag"""
    incident = _get_red_flag(_id)
    if len(incident) == 0:
        return jsonify({'status': 404, 'error': "Red-flag record not found"}), 404
    location = request.json.get('location', incident[0]['location'])
    if not isinstance(location, str):
        return jsonify({'status': 400, 'error': "Please use character strings"}), 400
    incident[0]['location'] = location
    return jsonify({"data":[{"id": incident[0]['id'], "message": "Updated red-flag record’s location"}], 'status': 200}), 200

@APP.route('/api/v1/red-flags/<int:_id>/comment', methods=['PATCH'])
def update_red_flag_comment(_id):
    """Function to edit comment of a red-flag"""
    incident = _get_red_flag(_id)
    if len(incident) == 0:
        return jsonify({'status': 404, 'error': "Red-flag record not found"}), 404
    comment = request.json.get('comment', incident[0]['comment'])
    if not isinstance(comment, str):
        return jsonify({'status': 400, 'error': "Please use character strings"}), 400
    incident[0]['comment'] = comment
    return jsonify({"data":[{"id": incident[0]['id'], "message": "Updated red-flag record’s comment"}], 'status': 200}), 200

if __name__ == "__main__":
    APP.run(debug=True)
