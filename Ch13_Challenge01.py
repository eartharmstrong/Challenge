class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return 2*self.width + 2*self.len

class Square():
    def __init__(self, w):
        self.width = w
    
    def area(self):
        return 4 * self.width

rec_peri = Rectangle(20, 10)
squ_peri = Square(10)

print(rec_peri.area())
print(squ_peri.area())




