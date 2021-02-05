"""front controller file"""


def front1(request):
    request['front1'] = "front1"


def front2(request):
    request['front2'] = "front2"


# front controllers function list
FRONT_CONTROLLER_FUNCTIONS = [
    front1,
    front2,
]
