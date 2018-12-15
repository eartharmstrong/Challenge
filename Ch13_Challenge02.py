class Square():
    def __init__(self, w):
        self.width = w
    
    def area(self):
        return 4 * self.width

    def change_size(self,newsize):
        self.width += newsize

squ_peri = Square(100)
print(squ_peri.area())

squ_peri.change_size(200)
print(squ_peri.width)





