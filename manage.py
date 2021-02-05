from wsgi_engine.wsgi import Application
from urls import urls
"""main file of server"""

application = Application(urls)
