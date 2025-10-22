from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from App.controllers.user import (
    create_employer, get_all_employers, get_user, update_username, update_fristname,
    update_lastname, update_password, delete_user
)

api_employer_views = Blueprint('api_employer_views', __name__, url_prefix='/api/employers')

@api_employer_views.route('/', methods=['GET'])
@jwt_required()
def list_employers():
    return jsonify([e.get_json() for e in get_all_employers()])

@api_employer_views.route('/<int:employer_id>', methods=['GET'])
@jwt_required()
def get_employer_detail(employer_id):
    employer = get_user(employer_id)
    if not employer or employer.role != 'employer':
        return jsonify({'error': 'Employer not found'}), 404
    return jsonify(employer.get_json())

@api_employer_views.route('/', methods=['POST'])
def create_employer_api():
    data = request.json
    employer = create_employer(
        data['username'], data['password'], data['first_name'], data['last_name'], data.get('company', 'Tech Corp')
    )
    return jsonify({'message': f"Employer created", 'id': employer.id}), 201

@api_employer_views.route('/<int:employer_id>', methods=['PUT'])
@jwt_required()
def update_employer(employer_id):
    data = request.json
    if 'username' in data:
        update_username(employer_id, data['username'])
    if 'first_name' in data:
        update_fristname(employer_id, data['first_name'])
    if 'last_name' in data:
        update_lastname(employer_id, data['last_name'])
    if 'password' in data:
        update_password(employer_id, data['password'])
    return jsonify({'message': 'Employer updated'})

@api_employer_views.route('/<int:employer_id>', methods=['DELETE'])
@jwt_required()
def delete_employer_api(employer_id):
    if delete_user(employer_id):
        return jsonify({'message': 'Employer deleted'})
    return jsonify({'error': 'Employer not found'}), 404
