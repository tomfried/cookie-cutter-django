import os

from .base import *
# you need to set "DJANGO_APP= 'prod'" as an environment variable in your OS
# (on which your website is hosted) if it is to be on production, else 'dev'.
if 'DJANGO_APP' in os.environ and os.environ['DJANGO_APP'] == 'prod':
    from .prod import *
else:
    from .dev import *
