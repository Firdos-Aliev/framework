import views
"""address manager"""

# можно передавать в request ссылки и их имена, чтобы можно было использовать в шаблонах
urls = {
    '/': views.index,
    '/hello/': views.hello,
    '/form/': views.form,
}
