from wsgi_engine.templater import render
"""views"""


def index(request):
    return "200", [b'index']


def hello(request):
    return "200", [render('templates/hello.html', object_list=[
        {'name': "name.0"},
        {'name': "name.1"},
        {'name': "name.2"}
    ]).encode('utf-8')]

