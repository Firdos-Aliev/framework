from wsgi_engine.templater import render
from logger import Logger
from patterns.decorators import debug

"""views"""

logger = Logger("logger")


@debug
def index(request):
    logger.log("info", "index")
    print(f"request: {request}")
    return "200", [render('index.html').encode('utf-8')]
