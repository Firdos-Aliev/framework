from templater import render


# любой контроллер должен возвращать код и html страницу принимая request
def index(request):
    return "200", [b'index']


def hello(request):
    return "200", [render('hello.html', object_list=[
        {'name': "name.0"},
        {'name': "name.1"},
        {'name': "name.2"}
    ]).encode('utf-8')]

