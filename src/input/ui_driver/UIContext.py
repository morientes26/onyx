

class UIContext:

    event = "onClick"
    x = 0
    y = 0
    action = None

    def __init__(self, event, x, y, action):
        self.event = event
        self.x = x
        self.y = y
        self.action = action

    def __str__(self):
        return __name__ + ' : ' + self.event + ' [' + str(self.x) + ', ' + str(self.y) + ', ' + self.action + ']'
