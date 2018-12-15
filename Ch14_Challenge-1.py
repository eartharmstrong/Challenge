class Square:
    square_list = []

    def __init__(self, m, l):
        self.m = m
        self.l = l
        self.square_list.append((self.m, self.l))

no1 = Square(10, 20)
no2 = Square(5, 10)

print(Square.square_list)


