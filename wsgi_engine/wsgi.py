from wsgi_engine.front_controllers_settings import FRONT_CONTROLLER_FUNCTIONS

"""wsgi server"""


def get_request_data(data):
    return_data = {}
    if data:
        for param in data.split('&'):
            key, item = param.split('=')
            return_data[key] = item
    return return_data


def get_post_data(environ):
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    request_body = environ['wsgi.input'].read(request_body_size)
    if request_body:
        data = get_request_data(request_body.decode('utf-8'))
    else:
        data = ''
    return data


class Application:

    def __init__(self, urls):
        # init obj with urls = {path: view}
        self.urls = urls

    def __call__(self, environ, start_response):

        # get method type
        method = environ['REQUEST_METHOD']
        # get data from get response
        request_data = get_request_data(environ['QUERY_STRING'])
        # get data from post response
        data = get_post_data(environ)

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
        request = dict()
        request['method'] = method
        request['request_data'] = request_data
        request['data'] = data
        # front controller functions
        for front in FRONT_CONTROLLER_FUNCTIONS:
            front(request)

        response_code, html_body = self.view(request)
        start_response(response_code, [('Content-Type', 'text/html')])
        return html_body
