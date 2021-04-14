import _sqlite3


class UserMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_user(self, id):
        request = "SELECT name FROM USER WHERE id=?"
        self.cursor.execute(request, (id,))
        result = self.cursor.fetchone()
        return result

    def edit_user(self, new_name, id):
        request = "UPDATE USER SET name=? WHERE id=?"
        self.cursor.execute(request, (new_name, id))
        self.connection.commit()

    def delete_user(self, id):
        request = "DELETE FROM USER WHERE id=?"
        self.cursor.execute(request, (id,))
        self.connection.commit()

