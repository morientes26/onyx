from abc import ABCMeta, abstractmethod


class AbstractActivity:

    __metaclass__ = ABCMeta

    active = None

    def __init__(self):
        self.activity = None

    def proccess(self, context):
        """
        Main activity method
        :param context: UIContext
        """
        tc = self.transform(context)
        self.on_proccess(tc)
        self.activity = self.get_activity(tc)
        if self.activity is not None:
            self.activity.proccess(tc)

    @abstractmethod
    def get_activity(self, transformed):
        """
        based on Context choose targeted Activity
        :param transformed: UCContext
        :raise NotImplementedError:
        """

    @abstractmethod
    def transform(self, context):
        """
        filter and transform to appropriate context
        from outsite/parent Context to ours Activity's Context
        :param context: UIContext
        :raise NotImplementedError:
        """

    @abstractmethod
    def on_proccess(self, transformed):
        """
        Proccess activity implementation
        :param transformed: UCContext
        :raise NotImplementedError:
        """