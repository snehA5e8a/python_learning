class AdultException(Exception):
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_minor_age(self):
        if self.age >= 18:
            raise AdultException('Exception: Person is adult')
        else:
            return self.age
    def display_person(self):
        try:
            print(f'Age: {self.get_minor_age()}')
        except AdultException as a:
            print(a)
        finally:
            print(f'Name: {self.name} and age as above') #can be given before try as name is unlikely to throw exception


h = Person('Hazel', 4)
h.display_person()

s = Person('sneha', 32)
s.display_person()

Person('Aiden', 5).display_person()


