class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-30)
y = AlwaysPositive(-20)
z = AlwaysPositive(-90)

print(x + y + z)
