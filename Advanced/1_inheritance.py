class food:
    def __init__(self, n, c, t):
        self.name = n
        self.calorie = c
        self.type = t
    def general(self):
        print(f'The calorie of {self.name} : {self.calorie}')
class veg(food):
    def __init__(self, n, c, t, k):
        super().__init__(n, c, t)
        self.color = k
    def speciality(self):
        if self.color == 'green':
            print(self.name, ' is the fibrous item with Iron')
        else:
            print(self.name, ' is a fibrous item may or may not with iron')
sp = veg('spinach', 250, 'fiber', 'green')
sp.speciality()
sp.general()
egg = food('egg', 60, 'protein')
egg.general()


