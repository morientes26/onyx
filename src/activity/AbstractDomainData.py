from abc import ABCMeta, abstractmethod

__author__ = 'morientes'


class AbstractDomainData:

    __metaclass__ = ABCMeta

    valid = False

    def __init__(self):
        self.valid = False

    @abstractmethod
    def validate(self):
        """
        validate domain data
        """

    @abstractmethod
    def invalidate(self):
        """
        invalidate domain data
        """
