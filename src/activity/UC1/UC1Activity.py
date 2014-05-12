from activity.AbstractActivity import AbstractActivity
from activity.UC1.UC1ActivityContext import UC1ActivityContext
from activity.UC1.UC1RenderedData import UC1RenderedData
from activity.UC1.UC1DomainData import UC1DomainData

__author__ = 'morientes'


class UC1Activity(AbstractActivity):

    activities = None

    def __init__(self):
        super(AbstractActivity, self).__init__()
        self.activities = None
        self.domain_data = UC1DomainData()

    def get_activity(self, context):
        #this activite do not return any activity
        return None

    def transform(self, context):
        #TODO:10-5-14:morientes - este mi nie je jasne ako budeme rozoberat context preto iba po svojom
        #       vyberam suradnice x, y a akciu
        return UC1ActivityContext(context.x, context.y, context.action)

    def on_proccess(self, context):
        print('--- Proccess [UC1Activity] ---')
        print(context)
        print('Printing x, y points ... [' + str(context.x) + ', ' + str(context.y) + '] ... done')

        self.domain_data.invalidate()

    def render(self, data):
        #TODO:12-5-14:morientes - implementovat. Zatial len provizorne tranformovanie dat
        #NOTE:12-5-14:morientes - Tu mi nie je jasne ako sa premnia domenove data na render data !!!
        uc1_rendered_data = UC1RenderedData()
        return uc1_rendered_data