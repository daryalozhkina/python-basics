# a = 'привет'
# print(type(a))
# print(dir(a))

class Door: # upper CamelCase
    def __init__(self):
        self.height = None
        self.width = None
        self.material = 0

class Car:
    def __init__(self):
    self.height = None
    self.width = None
    self.material = 0

user_1 = MyAdminUser()
# print(type(user_1))
# print(dir(user_1))
user_1.name = 'Иван'
user_1.age = 18
user_1.level = 2
print(user_1, )
