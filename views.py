from wsgi_engine.templater import render
from wsgi_engine.CBV import ListView
from models import Manager
from logger import Logger
from patterns.decorators import debug

"""views"""

manager = Manager()
logger = Logger("logger3")


@debug
def index(request):
    logger.log("info", "index")
    print(f"request: {request}")
    return "200", [render('index.html').encode('utf-8')]


@debug
def hello(request):
    logger.log("info", "hello")
    print(f"request: {request}")
    return "200", [render('hello.html', object_list=[
        {'name': "name-0"},
        {'name': "name-1"},
        {'name': "name-2"}
    ]).encode('utf-8')]


@debug
def form(request):
    logger.log("info", "form")
    print(f"request: {request}")
    return "200", [render('form.html').encode('utf-8')]


@debug
def users_list(request):
    logger.log("info", "users_list")
    print(f"request: {request}")
    users = manager.get_users()
    users_name = [f"{i.name} : {i}" for i in users]
    print(users_name)
    return "200", [render('users_list.html', users=users_name).encode('utf-8')]


@debug
def course_list(request):
    logger.log("info", "course_list")
    print(f"request: {request}")
    courses = manager.get_courses()
    cousres_name = [f"{i.name} : {i.category.name}" for i in courses]
    return "200", [render('courses_list.html', courses=cousres_name).encode('utf-8')]


@debug
def category_list(request):
    logger.log("info", "category_list")
    print(f"request: {request}")
    category = manager.get_categories()
    category_name = [i.name for i in category]
    return "200", [render('categories_list.html', categories=category_name).encode('utf-8')]


@debug
def add_category(request):
    logger.log("info", "add_category")
    print(f"request: {request}")
    if request['method'] == 'POST':
        name = request['data']['name']
        manager.add_category(name)
    else:
        return "200", [render('add_category.html').encode('utf-8')]
    return "200", [render('add_category.html').encode('utf-8')]


@debug
def add_composite_category(request):
    logger.log("info", "add_composite_category")
    print(f"request: {request}")
    if request['method'] == 'POST':
        name = request['data']['name']
        composite_category_name = request['data']['selected']

        manager.add_composite_to_composite(composite_category_name, name)
    else:
        categories = manager.get_categories()
        categories_name = [i.name for i in categories]
        return "200", [render('add_composite_category.html', categories=categories_name).encode('utf-8')]
    categories = manager.get_categories()
    categories_name = [i.name for i in categories]
    return "200", [render('add_composite_category.html', categories=categories_name).encode('utf-8')]


@debug
def add_user(request):
    logger.log("info", "add_user")
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


@debug
def add_course(request):
    logger.log("info", "add_course")
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


@debug
def add_user_to_course(request):
    if request["method"] == "POST":

        user_name = request['data']['name']
        course_name = request['data']['courses']
        course_replaced = course_name.replace("+", " ")
        user = manager.get_user_by_name(user_name)
        course = manager.get_course_by_name(course_replaced)
        course.add_user(user)
    else:
        courses = [i.get_name() for i in manager.get_courses()]
        return "200", [render('add_user_to_course.html', courses=courses).encode('utf-8')]
    courses = [course.get_name() for course in manager.get_courses()]
    return "200", [render('add_user_to_course.html', courses=courses).encode('utf-8')]


class AllStudents(ListView):
    template_name = "students.html"

    def query_set(self):
        users = manager.get_users()
        users_name = [f"{i.name} : {i}" for i in users if i.__str__() == "студент"]
        return users_name

    def logger(self):
        logger.log("info", "AllStudents CBV")

