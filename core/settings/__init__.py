import os

environment = os.environ.get("DJANGO_SETTINGS_MODULE", "core.settings.dev")

if environment == "core.settings.prod":
    from .prod import *
else:
    from .dev import *
