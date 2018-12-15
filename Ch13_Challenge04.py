class Horse():
    def __init__(self, size, color, rider):
        self.size = size
        self.color = color
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

rider_name = Rider("Kengo")
horse = Horse("big", "red",rider_name)

print(horse.rider.name)
