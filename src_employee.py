
class Employee:
    def __init__(self, name, id, position):
        self.name = name
        self.id = id
        self.position = position

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Position: {self.position}"
