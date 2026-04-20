import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'focusflow.focusflow.settings'   # ✅ THIS IS THE FIX
)

application = get_wsgi_application()