import views

# можно вставить любой новый контроллер на любой другой url, который пожелаешь
urls = {
    '/': views.index,
    '/hello/': views.hello,
}
