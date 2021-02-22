from jinja2 import FileSystemLoader, Template
from jinja2.environment import Environment

"""template engine"""


def render(template_name, folder='templates', **kwargs):
    """render function template"""
    environment = Environment(loader=FileSystemLoader(folder))
    template = environment.get_template(template_name)
    return template.render(**kwargs)


if __name__ == '__main__':
    test = render('hello.html', folder='../templates', object_list=[
        {'name': "name1"},
        {'name': "name2"},
        {'name': "name3"}
    ], name=["user", "user2", "user3"])
    print(type(test))
    print(test)
    print(test.encode('utf-8'))
    print(type(test.encode('utf-8')))
