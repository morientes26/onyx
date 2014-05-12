from activity.AbstractRenderedData import AbstractRenderedData

__author__ = 'morientes'


class Point(AbstractRenderedData):

    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y