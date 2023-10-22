#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    response = Response('A WSGI generated this response!')
    return response

if __name__ == '__main__':
    run_simple('localhost', 5555, application)
