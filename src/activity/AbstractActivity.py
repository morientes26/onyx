from abc import ABCMeta, abstractmethod

__author__ = 'morientes'


class AbstractActivity:

    __metaclass__ = ABCMeta

    active = None
    domain_data = None

    def __init__(self, domain_data):
        self.activity = None
        self.domain_data = domain_data

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

    def draw(self, data):
        """
        Draw data
        :param data: AbstractRenderedData
        :raise NotImplementedError:
        """
        self.render(data)
        self.domain_data.validate()

    @abstractmethod
    def get_activity(self, transformed):
        """
        based on Context choose targeted Activity
        :param transformed: UCContext
        :return appropriate Activity (MainActivity...)
        :raise NotImplementedError:
        """

    @abstractmethod
    def transform(self, context):
        """
        filter and transform to appropriate context
        from outsite/parent Context to ours Activity's Context
        :param context: UIContext
        :return appropriate object Context (MainActivityContext...)
        :raise NotImplementedError:
        """

    @abstractmethod
    def on_proccess(self, transformed):
        """
        Proccess activity implementation
        :param transformed: UCContext
        :raise NotImplementedError:
        """

    @abstractmethod
    def render(self, data):
        """
        Transform DomainData to RenderedData
        :param data: DomainData
        :return appropriate RenderedData (MainRenderedData...)
        :raise NotImplementedError:
        """