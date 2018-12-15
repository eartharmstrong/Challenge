class Square:

    def __init__(self, m):
        self.m = m
    
    def __repr__(self):
        return "{} by {} by {}".format(self.m, self.m, self.m)

no1 = Square(10)

print(no1)


