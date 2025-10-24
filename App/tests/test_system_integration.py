import pytest
from unittest import TestCase
from App.main import create_app
from App.database import db, create_db
from App.controllers import (
    create_student, create_staff, create_employer,
    create_internship_position, add_to_shortlist,
    get_shortlists_position, update_position_title
)

class TestSystemIntegration(TestCase):
    """System integration tests for complete business workflows"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test_integration.db'})
        create_db()
        yield
        db.drop_all()

    def test_complete_internship_workflow_integration(self):
        """Integration test for the complete internship workflow including user creation,
        position creation, shortlisting, and updates"""
        # Create users
        employer = create_employer("company", "pass123", "Tech", "Corp", "TechCorp Inc")
        staff = create_staff("staffmember", "pass123", "Staff", "Member", "HR Manager")
        student = create_student("student", "pass123", "John", "Student", "Computer Science")
        
        # Create internship position
        position = create_internship_position(
            employer.id,
            "Software Developer Intern",
            "Development position",
            "Python, JavaScript"
        )
        
        # Staff shortlists student
        shortlist = add_to_shortlist(staff.id, student.id, position.id)
        
        # Update position
        update_position_title(position.id, "Senior Developer Intern")
        
        # Verify shortlist
        shortlists = get_shortlists_position(position.id)
        self.assertEqual(len(shortlists), 1)
        self.assertEqual(shortlists[0].student_id, student.id)

    def test_multiple_students_shortlist_integration(self):
        """Integration test for handling multiple students in the shortlisting process"""
        # Create employer and position
        employer = create_employer("company2", "pass123", "Tech", "Corp", "TechCorp Inc")
        position = create_internship_position(
            employer.id,
            "Junior Developer",
            "Entry level position",
            "Python knowledge"
        )
        
        # Create staff member
        staff = create_staff("staffmember2", "pass123", "Staff", "Member", "HR Manager")
        
        # Create multiple students
        student1 = create_student("student1", "pass123", "John", "Doe", "Computer Science")
        student2 = create_student("student2", "pass123", "Jane", "Smith", "Software Engineering")
        
        # Shortlist both students
        shortlist1 = add_to_shortlist(staff.id, student1.id, position.id)
        shortlist2 = add_to_shortlist(staff.id, student2.id, position.id)
        
        # Verify shortlists
        shortlists = get_shortlists_position(position.id)
        self.assertEqual(len(shortlists), 2)
        student_ids = [s.student_id for s in shortlists]
        self.assertIn(student1.id, student_ids)
        self.assertIn(student2.id, student_ids)