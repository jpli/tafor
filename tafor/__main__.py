import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tafor import conf
from tafor.app.main import main


if __name__ == '__main__':
    main()