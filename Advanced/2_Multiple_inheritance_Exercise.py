class Teacher:
    def __init__(self, educ):
        self.education = educ

    def occup(self):
        print(f"My education is {self.education}")
        if self.education == 'BEd':
            print('I can be a Teacher')


class Student:
    def hobby(self, hobbies):
        hobby_str = ''
        for ho in hobbies:
            hobby_str += ho + ', '
        hobby_str = hobby_str[:-2]
        print(f'My Hobbies are {hobby_str}')


class Youtuber:
    def passion(self, passions):
        passion_string = ''
        for pas in passions:
            passion_string += str(pas) + ', '
        passion_string = passion_string[:-2]
        print(f'My passions are {passion_string}')
        if 'content creation' in passions:
            print('I like to be a Youtuber')


class Person(Teacher, Student, Youtuber):
    def __init__(self, name, educ): #proper initialisation - parent's method called, it follows method resolution order (multiple inheritance cases)
        super().__init__(name)
        self.name = name

    def name_print(self):
        print(f'My name is {self.name}')


Sophia = Person('Sophia John', 'BEd')
Sophia.name_print()
Sophia.passion(['content creation', 'Drawing', 'Parenting'])

abin = Person('Abin', 'Engineering')
abin.name_print()
abin.hobby(['reading', 'writing', 'content creation'])
abin.passion(['reading', 'writing', 'content creation'])
