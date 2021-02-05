from wsgi_engine.front_controllers_settings import FRONT_CONTROLLER_FUNCTIONS
"""wsgi server"""


class Application:

    def __init__(self, urls):
        # init obj with urls = {path: view}
        self.urls = urls

    def __call__(self, environ, start_response):

        # add '/' to end of path
        path = environ['PATH_INFO']
        if path[-1] != '/':
            path += '/'

        # find correct path
        if path in self.urls:
            self.view = self.urls[path]
        else:
            start_response('404', [('Content-Type', 'text/html')])
            return [b'<h1>Not found 404!<h1>']

        # fill request
        request = {}
        # front controller functions
        for front in FRONT_CONTROLLER_FUNCTIONS:
            front(request)

        response_code, html_body = self.view(request)
        start_response(response_code, [('Content-Type', 'text/html')])
        return html_body

