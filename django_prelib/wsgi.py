"""
WSGI config for django_prelib project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_prelib.settings")

from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD

=======
>>>>>>> ba40893cfc03f3c84497840daff9d73f4c62a4e5
application = get_wsgi_application()
