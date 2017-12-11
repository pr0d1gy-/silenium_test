#!/usr/bin/env python
from arguments_parser import parser
from application import Application


if __name__ == '__main__':
    arguments = parser.parse_args()
    try:
        app = Application(arguments)
        app.run()
        app.close()
    except Exception as e:
        print('\033[1;31m{}:\033[1;m'.format(e.__class__.__name__), e)
    finally:
        if 'app' in locals():
            app.close()
