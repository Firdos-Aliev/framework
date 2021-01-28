from jinja2 import Template


def render(template, **kwargs):
    with open(template, encoding='utf-8') as file:
        template = Template(file.read())
    return template.render(**kwargs)


if __name__ == '__main__':
    test = render('hello.html', object_list=[
        {'name': "name1"},
        {'name': "name2"},
        {'name': "name3"}
    ])
    print(type(test))
    print(test)
    print(test.encode('utf-8'))
    print(type(test.encode('utf-8')))
