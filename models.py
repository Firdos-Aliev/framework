import abc


class User(abc.ABC):

    def __init__(self, name):
        self.name = name


class Teacher(User):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "учитель"


class Student(User):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "студент"


class UserFactory(abc.ABC):
    """factory method"""

    @abc.abstractmethod
    def create_user(self, name) -> User:
        pass


class TeacherFactory(UserFactory):

    def create_user(self, name) -> User:
        return Teacher(name)


class StudentFactory(UserFactory):

    def create_user(self, name) -> User:
        return Student(name)


#########################################################################

class Category:

    def __init__(self, name):
        self.name = name


#########################################################################

class Course:

    def __init__(self, name, category: Category):
        self.name = name
        self.category = category
        self.students = []
        self.teachers = []


class Manager:
    # добавил несколько обьектов, что при запуске не было пустым
    users = [Student("user1"), Student("user2"), Teacher("teacher1")]
    categories = [Category("JS"), Category("Python"), Category("C++")]
    courses = [Course("Основы Python", categories[1]),
               Course("Продвинутый Python", categories[1]),
               Course("С++ для маленьких", categories[2])]

    def create_factory(self, user_type: str) -> UserFactory:
        type_list = {
            "teacher": TeacherFactory,
            "student": StudentFactory,
        }
        return type_list[user_type]()

    def add_user(self, user: User):
        self.users.append(user)

    def get_users(self):
        return self.users

    def add_category(self, name):
        category = Category(name)
        self.categories.append(category)
        return category

    def get_category_by_name(self, name):
        for i in self.categories:
            if i.name == name:
                return i
        return ""

    def get_categories(self):
        return self.categories

    def add_course(self, name, category: Category):
        course = Course(name, category)
        self.courses.append(course)
        return course

    def get_courses(self):
        return self.courses


def test_client_code(factory: UserFactory, name) -> User:
    print(factory)
    user = factory.create_user(name)
    print(type(user))
    print(user.name)
    return user


if __name__ == "__main__":
    factory = Manager.create_factory('student')
    # factory = manager.create_factory("teacher")
    user = factory.create_user("user-1")
    print(user.name)
    print(type(user))
