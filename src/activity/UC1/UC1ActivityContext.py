
class UC1ActivityContext:

    x = 0
    y = 0
    action = None

    def __init__(self, x, y, action):
        self.x = x
        self.y = y
        self.action = action

    def __str__(self):
        return __name__ + ' : ' + str(self.x) + ', ' + str(self.y) + ', ' + self.action
