import sys
import os
from project import setting
from project.app import create_app

if __name__ == '__main__':
    if sys.argv[1] == 'run':
        app = create_app()
        app.run(
            host=setting.HOST,
            port=setting.PORT,
            debug=setting.DEBUG,
        )