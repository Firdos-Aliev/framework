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

class CategoryComponent(abc.ABC):

    @abc.abstractmethod
    def show(self):
        pass


class Category(CategoryComponent):

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


class CompositeCategory(CategoryComponent):
    def __init__(self, name):
        self.name = name
        self.categories = []

    def get_name(self):
        return self.name

    def show(self):
        for i in self.categories:
            i.show()

    def add(self, category):
        self.categories.append(category)

    def delete(self, category):
        self.categories.remove(category)


#########################################################################

class Course:

    def __init__(self, name, category: CompositeCategory):
        self.name = name
        self.category = category
        self.students = []
        self.teachers = []


cat1 = Category("cat1")
cat2 = Category("cat2")
cat3 = Category("cat3")
cat4 = Category("cat4")
cat5 = Category("cat5")

composite1 = CompositeCategory("cop1")
composite2 = CompositeCategory("cop2")

composite1.add(cat1)
composite1.add(cat2)
composite1.add(cat3)

composite2.add(cat4)
composite2.add(cat5)


class Manager:
    # добавил несколько обьектов, что при запуске не было пустым
    users = [Student("user1"), Student("user2"), Teacher("teacher1")]
    categories = [composite1, composite2]
    courses = [Course("Основы Python", categories[0]),
               Course("Продвинутый Python", categories[0]),
               Course("С++ для маленьких", categories[1])]

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
        category = CompositeCategory(name)
        self.categories.append(category)
        return category

    def add_category_to_composite(self, composite_name, category_name):
        for i in self.categories:
            if i.name == composite_name:
                i.add(Category(category_name))

    def add_composite_to_composite(self, name1, name2):
        for i in self.categories:
            if i.name == name1:
                i.add(CompositeCategory(name2))
                return

        self.categories.append(CompositeCategory(name2))

    def get_category_by_name(self, name):
        for i in self.categories:
            if i.name == name:
                return i
        return ""

    def get_categories(self):
        return self.categories

    def add_course(self, name, category: CompositeCategory):
        course = Course(name, category)
        self.courses.append(course)
        return course

    def get_courses(self):
        return self.courses


if __name__ == "__main__":
    cat1 = Category("cat1")
    cat2 = Category("cat2")
    cat3 = Category("cat3")
    cat4 = Category("cat4")
    cat5 = Category("cat5")

    composite1 = CompositeCategory("cop1")
    composite2 = CompositeCategory("cop2")

    composite1.add(cat1)
    composite1.add(cat2)
    composite1.add(cat3)

    composite2.add(cat4)
    composite2.add(cat5)

    composite1.add(composite2)

    composite1.show()
    print("----------------")
    composite2.show()
