from wsgi_engine.templater import render
"""views"""


def index(request):
    print(f"request: {request}")
    return "200", [b'index']


def hello(request):
    print(f"request: {request}")
    return "200", [render('hello.html', object_list=[
        {'name': "name.0"},
        {'name': "name.1"},
        {'name': "name.2"}
    ]).encode('utf-8')]


def form(request):
    print(f"request: {request}")
    return "200", [render('form.html').encode('utf-8')]
