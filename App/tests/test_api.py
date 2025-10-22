import pytest
from App.main import create_app
from App.database import db, create_db
from flask_jwt_extended import create_access_token
from App.controllers import (
    create_student, create_staff, create_employer, create_internship_position, add_to_shortlist
)

def get_auth_header(user):
    token = create_access_token(identity=user.id)
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture(scope='module')
def test_client():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test_api.db'})
    create_db()
    with app.test_client() as client:
        with app.app_context():
            yield client
    db.drop_all()

def test_user_crud(test_client):
    # Create user
    res = test_client.post('/api/users/', json={
        'username': 'alice', 'password': 'alicepass', 'role': 'student', 'first_name': 'Alice', 'last_name': 'Smith'
    })
    assert res.status_code == 201
    # Login to get JWT
    student = create_student('bob', 'bobpass', 'Bob', 'Brown')
    auth_header = get_auth_header(student)
    # Get users (protected)
    res = test_client.get('/api/users/', headers=auth_header)
    assert res.status_code == 200
    # Update user
    res = test_client.put(f'/api/users/{student.id}', json={'first_name': 'Bobby'}, headers=auth_header)
    assert res.status_code == 200
    # Delete user
    res = test_client.delete(f'/api/users/{student.id}', headers=auth_header)
    assert res.status_code == 200

def test_internship_crud(test_client):
    employer = create_employer('emp1', 'pass', 'Emp', 'Loyer', 'CompanyX')
    auth_header = get_auth_header(employer)
    # Create internship
    res = test_client.post('/api/internships/', json={
        'employer_id': employer.id, 'title': 'Dev Intern', 'description': 'Work on code', 'requirements': 'Python'
    })
    assert res.status_code == 201
    # List internships
    res = test_client.get('/api/internships/', headers=auth_header)
    assert res.status_code == 200

def test_shortlist_crud(test_client):
    staff = create_staff('staff1', 'pass', 'Staff', 'One', 'HR')
    student = create_student('stud1', 'pass', 'Stud', 'Ent', 'CS')
    employer = create_employer('emp2', 'pass', 'Emp', 'Loyer', 'CompanyY')
    position = create_internship_position(employer.id, 'QA Intern', 'Test stuff', 'Testing')
    auth_header = get_auth_header(staff)
    # Add to shortlist
    res = test_client.post('/api/shortlists/', json={
        'staff_id': staff.id, 'student_id': student.id, 'position_id': position.id
    }, headers=auth_header)
    assert res.status_code == 201
    # List shortlists
    res = test_client.get('/api/shortlists/', headers=auth_header)
    assert res.status_code == 200
