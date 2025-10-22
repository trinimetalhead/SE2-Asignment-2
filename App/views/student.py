from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from App.controllers.user import (
    create_student, get_all_students, get_user, update_username, update_firstname,
    update_lastname, update_password, delete_user
)

api_student_views = Blueprint('api_student_views', __name__, url_prefix='/api/students')

@api_student_views.route('/', methods=['GET'])
@jwt_required()
def list_students():
    return jsonify([s.get_json() for s in get_all_students()])

@api_student_views.route('/<int:student_id>', methods=['GET'])
@jwt_required()
def get_student_detail(student_id):
    student = get_user(student_id)
    if not student or student.role != 'student':
        return jsonify({'error': 'Student not found'}), 404
    return jsonify(student.get_json())

@api_student_views.route('/', methods=['POST'])
def create_student_api():
    data = request.json
    student = create_student(
        data['username'], data['password'], data['first_name'], data['last_name'], data.get('major', 'Undeclared')
    )
    return jsonify({'message': f"Student created", 'id': student.id}), 201

@api_student_views.route('/<int:student_id>', methods=['PUT'])
@jwt_required()
def update_student(student_id):
    data = request.json
    if 'username' in data:
        update_username(student_id, data['username'])
    if 'first_name' in data:
        update_firstname(student_id, data['first_name'])
    if 'last_name' in data:
        update_lastname(student_id, data['last_name'])
    if 'password' in data:
        update_password(student_id, data['password'])
    return jsonify({'message': 'Student updated'})

@api_student_views.route('/<int:student_id>', methods=['DELETE'])
@jwt_required()
def delete_student_api(student_id):
    if delete_user(student_id):
        return jsonify({'message': 'Student deleted'})
    return jsonify({'error': 'Student not found'}), 404
