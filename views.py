from wsgi_engine.templater import render
from models import Manager

"""views"""

manager = Manager()


def index(request):
    print(f"request: {request}")
    return "200", [render('index.html').encode('utf-8')]


def hello(request):
    print(f"request: {request}")
    return "200", [render('hello.html', object_list=[
        {'name': "name-0"},
        {'name': "name-1"},
        {'name': "name-2"}
    ]).encode('utf-8')]


def form(request):
    print(f"request: {request}")
    return "200", [render('form.html').encode('utf-8')]


def users_list(request):
    print(f"request: {request}")
    users = manager.get_users()
    users_name = [f"{i.name} : {i}" for i in users]
    print(users_name)
    return "200", [render('users_list.html', users=users_name).encode('utf-8')]


def course_list(request):
    print(f"request: {request}")
    courses = manager.get_courses()
    cousres_name = [f"{i.name} : {i.category.name}" for i in courses]
    return "200", [render('courses_list.html', courses=cousres_name).encode('utf-8')]


def category_list(request):
    print(f"request: {request}")
    category = manager.get_categories()
    category_name = [i.name for i in category]
    return "200", [render('categories_list.html', categories=category_name).encode('utf-8')]


def add_category(request):
    print(f"request: {request}")
    if request['method'] == 'POST':
        name = request['data']['name']
        manager.add_category(name)
    else:
        return "200", [render('add_category.html').encode('utf-8')]
    return "200", [render('add_category.html').encode('utf-8')]


def add_user(request):
    print(f"request: {request}")
    if request['method'] == 'POST':
        # take data
        name = request['data']['name']
        factory_type = request['data']['type']
        # create user
        factory = manager.create_factory(factory_type)
        user = factory.create_user(name)
        # add to manager
        manager.add_user(user)
    else:
        return "200", [render('add_user.html').encode('utf-8')]
    return "200", [render('add_user.html').encode('utf-8')]


def add_course(request):
    print(f"request: {request}")
    if request['method'] == 'POST':
        # take data
        name = request['data']['name']
        category = request['data']['selected']
        category_obj = manager.get_category_by_name(category)
        manager.add_course(name, category_obj)
    else:
        categories = manager.get_categories()
        categories_name = [i.name for i in categories]
        return "200", [render('add_course.html', categories=categories_name).encode('utf-8')]
    categories = manager.get_categories()
    categories_name = [i.name for i in categories]
    return "200", [render('add_course.html', categories=categories_name).encode('utf-8')]


if "__main__" == __name__:
    pass
