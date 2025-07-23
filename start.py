from waitress import serve
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Gestion_Diaconales.settings")

application = get_wsgi_application()
serve(application, host='127.0.0.1', port=8000)
