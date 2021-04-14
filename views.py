from wsgi_engine.templater import render
from logger import Logger
from patterns.decorators import debug

"""views"""

logger = Logger("logger")


@debug
def index(request):
    logger.log("info", "index")
    context = {
        "title": "index"
    }
    print(f"request: {request}")
    return "200", [render('index.html', **context).encode('utf-8')]
