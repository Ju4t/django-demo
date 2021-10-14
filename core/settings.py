import os

if os.environ.get('PRODUCT', 0):
    from .settings_pro import *
else:
    from .settings_dev import *
