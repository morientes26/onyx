from abc import ABCMeta, abstractmethod

__author__ = 'morientes'


class AbstractRenderedData:

    __metaclass__ = ABCMeta

    draw_list = []

    def __init__(self, draw_list):
        """
        Constructor of class
        :param draw_list: Drawable
        """
        self.draw_list = draw_list