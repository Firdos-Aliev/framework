def front1(request):
    request['front1'] = "front1"


def front2(request):
    request['front2'] = "front2"


# можно добавить любой front controller который пожелаешь, просто вставив функции в список
FRONT_CONTROLLER_FUNCTIONS = [
    front1,
    front2,
]
