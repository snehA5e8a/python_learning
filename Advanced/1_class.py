class Meals:
    def __init__(self,t,m,s):
        self.type = t
        self.main = m
        self.side = s

    def menu(self):
        print('You have ', m, ' for ', t)
    def nutri(self):
        if self.side == 'egg' or 'cherupayar':
            print('There is protein in your side dish, ', self.side)
        else:
            print('No protein found in your ', s)

t = input('The type of course: ')
m = input('Enter the main course: ')
s = input('The side dish: ')
Meals(t,m,s).menu()
print(Meals(t,m,s).nutri())
