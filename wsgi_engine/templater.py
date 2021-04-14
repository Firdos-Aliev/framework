from jinja2 import FileSystemLoader, Template
from jinja2.environment import Environment

"""template engine"""


def render(template_name, folder='templates', **kwargs):
    """render function template"""
    environment = Environment(loader=FileSystemLoader(folder))
    template = environment.get_template(template_name)
    return template.render(**kwargs)

