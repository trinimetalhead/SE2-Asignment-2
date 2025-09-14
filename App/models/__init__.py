from .user import User
from .student import Student
from .staff import Staff
from .employer import Employer
from .internship_position import InternshipPosition
from .shortlist import Shortlist

# Make them available for import
__all__ = ['User', 'Student', 'Staff', 'Employer', 'InternshipPosition', 'Shortlist']
