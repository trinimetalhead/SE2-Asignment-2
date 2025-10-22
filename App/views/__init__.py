# blue prints are imported 
# explicitly instead of using *
from .user import api_user_views
from .index import index_views
from .auth import auth_views
from .admin import setup_admin
from .internship import api_internship_views
from .shortlist import api_shortlist_views


views = [api_user_views, index_views, auth_views, api_internship_views, api_shortlist_views] 
# blueprints must be added to this list