import abc
from wsgi_engine.templater import render


class View(abc.ABC):
    template_name = ""
    query = []
    request = {}

    def __call__(self, *args, **kwargs):
        self.logger()
        self.query_set()
        return self.html_response()

    def logger(self):
        pass

    def html_response(self):
        pass

    def query_set(self):
        pass


class ListView(View):

    def query_set(self):
        query = self.query
        return query

    def html_response(self):
        return "200", [render(self.template_name, object_list=self.query_set()).encode('utf-8')]
