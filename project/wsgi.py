from django.core.wsgi import get_wsgi_application
import os
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJECT_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.settings')

application = get_wsgi_application()
