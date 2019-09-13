"""
SplitCalculator development configuration.

Andrew DeOrio <awdeorio@umich.edu>
"""

import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\xc7\t2\xbb1\xe2\xea\x8apWx\x05\x86\xe9\\"YS\xcd\x1e\x84\xe8+\x88'  # noqa: E501  pylint: disable=line-too-long
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'uploads'
)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/splitCalculator.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'splitCalculator.sqlite3'
)