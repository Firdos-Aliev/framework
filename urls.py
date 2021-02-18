import views

"""address manager"""

# можно передавать в request ссылки и их имена, чтобы можно было использовать в шаблонах
urls = {
    '/': views.index,
    '/hello/': views.hello,
    '/form/': views.form,
    '/users/': views.users_list,
    '/courses/': views.course_list,
    '/categories/': views.category_list,
    '/add_user/': views.add_user,
    '/add_course/': views.add_course,
    '/add_category/': views.add_category,
    '/add_composite_category/': views.add_composite_category,
}
