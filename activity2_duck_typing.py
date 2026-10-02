class Car:
    def move(self):
        return "The car is driving."


class Person:
    def move(self):
        return "The person is walking."


class Robot:
    def move(self):
        return "The robot is moving."


def make_it_move(entity):
    print(entity.move())

if __name__ == "__main__":
    objects = [Car(), Person(), Robot()]

    for obj in objects:
        make_it_move(obj)