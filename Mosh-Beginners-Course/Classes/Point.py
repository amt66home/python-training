    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)

# if you want to change x to 11
point.x = 11

# print point x
print(point.x)