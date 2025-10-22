from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from App.controllers.user import (
    create_staff, get_all_staff, get_user, update_username, update_firstname,
    update_lastname, update_password, delete_user
)

api_staff_views = Blueprint('api_staff_views', __name__, url_prefix='/api/staff')

@api_staff_views.route('/', methods=['GET'])
@jwt_required()
def list_staff():
    return jsonify([s.get_json() for s in get_all_staff()])

@api_staff_views.route('/<int:staff_id>', methods=['GET'])
@jwt_required()
def get_staff_detail(staff_id):
    staff = get_user(staff_id)
    if not staff or staff.role != 'staff':
        return jsonify({'error': 'Staff not found'}), 404
    return jsonify(staff.get_json())

@api_staff_views.route('/', methods=['POST'])
def create_staff_api():
    data = request.json
    staff = create_staff(
        data['username'], data['password'], data['first_name'], data['last_name'], data.get('position', 'Staff')
    )
    return jsonify({'message': f"Staff created", 'id': staff.id}), 201

@api_staff_views.route('/<int:staff_id>', methods=['PUT'])
@jwt_required()
def update_staff(staff_id):
    data = request.json
    if 'username' in data:
        update_username(staff_id, data['username'])
    if 'first_name' in data:
        update_firstname(staff_id, data['first_name'])
    if 'last_name' in data:
        update_lastname(staff_id, data['last_name'])
    if 'password' in data:
        update_password(staff_id, data['password'])
    return jsonify({'message': 'Staff updated'})

@api_staff_views.route('/<int:staff_id>', methods=['DELETE'])
@jwt_required()
def delete_staff_api(staff_id):
    if delete_user(staff_id):
        return jsonify({'message': 'Staff deleted'})
    return jsonify({'error': 'Staff not found'}), 404
