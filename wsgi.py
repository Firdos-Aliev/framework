from urls import urls
from settings import FRONT_CONTROLLER_FUNCTIONS


class Application:

    def __call__(self, environ, start_response):

        path = environ['PATH_INFO']
        if path[-1] != '/':
            path += '/'

        if path in urls:
            self.view = urls[path]
        else:
            start_response('404', [('Content-Type', 'text/html')])
            return [b'<h1>Not found 404!<h1>']

        request = {}
        for front in FRONT_CONTROLLER_FUNCTIONS:
            front(request)

        response_code, html_body = self.view(request)
        start_response(response_code, [('Content-Type', 'text/html')])
        return html_body


application = Application()
