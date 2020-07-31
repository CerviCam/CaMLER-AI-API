import sys
import os
from project import setting
from project.app import run_app

if __name__ == '__main__':
    if sys.argv[1] == 'run':
        run_app(
            host=setting.HOST,
            port=setting.PORT,
            debug=setting.DEBUG,
        )