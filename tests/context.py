# this is based on https://docs.python-guide.org/writing/structure/#test-suite
# (which conflicts with https://docs.pytest.org/en/6.2.x/goodpractices.html, to which we can switch later)
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import haierlib
from haierlib.parsers import parse_resp