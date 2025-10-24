import unittest
from App.models import Student, Staff, Employer, InternshipPosition, Shortlist
from datetime import datetime

class TestStudentUnit(unittest.TestCase):
    """Unit tests for Student model"""
    
    def test_new_student_creation(self):
        """Unit test: Verify student object creation with correct attributes"""
        student = Student("john", "pass123", "John", "Doe", "Computer Science")
        self.assertEqual(student.username, "john")
        self.assertEqual(student.major, "Computer Science")
        self.assertEqual(student.role, "student")

    def test_student_json_serialization(self):
        """Unit test: Verify student JSON serialization is correct"""
        student = Student("john", "pass123", "John", "Doe", "Computer Science")
        json_data = student.get_json()
        self.assertEqual(json_data["major"], "Computer Science")
        self.assertEqual(json_data["role"], "student")

class TestStaffUnit(unittest.TestCase):
    """Unit tests for Staff model"""
    
    def test_new_staff_creation(self):
        """Unit test: Verify staff object creation with correct attributes"""
        staff = Staff("jane", "pass123", "Jane", "Smith", "Lecturer")
        self.assertEqual(staff.username, "jane")
        self.assertEqual(staff.position, "Lecturer")
        self.assertEqual(staff.role, "staff")

    def test_staff_json_serialization(self):
        """Unit test: Verify staff JSON serialization is correct"""
        staff = Staff("jane", "pass123", "Jane", "Smith", "Lecturer")
        json_data = staff.get_json()
        self.assertEqual(json_data["position"], "Lecturer")
        self.assertEqual(json_data["role"], "staff")

class TestEmployerUnit(unittest.TestCase):
    """Unit tests for Employer model"""
    
    def test_new_employer_creation(self):
        """Unit test: Verify employer object creation with correct attributes"""
        employer = Employer("company", "pass123", "Company", "Inc", "Tech Corp")
        self.assertEqual(employer.username, "company")
        self.assertEqual(employer.company, "Tech Corp")
        self.assertEqual(employer.role, "employer")

    def test_employer_json_serialization(self):
        """Unit test: Verify employer JSON serialization is correct"""
        employer = Employer("company", "pass123", "Company", "Inc", "Tech Corp")
        json_data = employer.get_json()
        self.assertEqual(json_data["company"], "Tech Corp")
        self.assertEqual(json_data["role"], "employer")

class TestInternshipPositionUnit(unittest.TestCase):
    """Unit tests for InternshipPosition model"""
    
    def test_new_position_creation(self):
        """Unit test: Verify internship position object creation with correct attributes"""
        position = InternshipPosition("Developer", "Job Description", "Requirements", 1)
        self.assertEqual(position.title, "Developer")
        self.assertEqual(position.description, "Job Description")
        self.assertEqual(position.requirements, "Requirements")
        self.assertEqual(position.employer_id, 1)

    def test_position_json_serialization(self):
        """Unit test: Verify internship position JSON serialization is correct"""
        position = InternshipPosition("Developer", "Job Description", "Requirements", 1)
        json_data = position.get_json()
        self.assertEqual(json_data["title"], "Developer")
        self.assertEqual(json_data["description"], "Job Description")