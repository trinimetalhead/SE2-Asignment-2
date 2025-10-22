from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from App.controllers import (
    add_to_shortlist, get_shortlist_id, get_all_shortlists,
    get_shortlists_student, get_shortlists_position, get_shortlists_staff,
    update_shortlist_status, delete_shortlist
)

api_shortlist_views = Blueprint('api_shortlist_views', __name__, url_prefix='/api/shortlists')

@api_shortlist_views.route('/', methods=['GET'])
@jwt_required()
def list_shortlists():
    return jsonify([s.get_json() for s in get_all_shortlists()])

@api_shortlist_views.route('/<int:shortlist_id>', methods=['GET'])
@jwt_required()
def get_shortlist(shortlist_id):
    shortlist = get_shortlist_id(shortlist_id)
    if not shortlist:
        return jsonify({'error': 'Shortlist not found'}), 404
    return jsonify(shortlist.get_json())

@api_shortlist_views.route('/', methods=['POST'])
@jwt_required()
def create_shortlist():
    data = request.json
    shortlist = add_to_shortlist(
        data['staff_id'], data['student_id'], data['position_id']
    )
    return jsonify({'message': 'Shortlist created', 'id': shortlist.id}), 201

@api_shortlist_views.route('/<int:shortlist_id>', methods=['PUT'])
@jwt_required()
def update_shortlist(shortlist_id):
    data = request.json
    if 'status' in data:
        update_shortlist_status(shortlist_id, data['status'])
    return jsonify({'message': 'Shortlist updated'})

@api_shortlist_views.route('/<int:shortlist_id>', methods=['DELETE'])
@jwt_required()
def delete_shortlist_api(shortlist_id):
    delete_shortlist(shortlist_id)
    return jsonify({'message': 'Shortlist deleted'})
