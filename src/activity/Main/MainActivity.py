from activity.AbstractActivity import AbstractActivity
from activity.UC1.UC1Activity import UC1Activity
from activity.Main.MainActivityContext import MainActivityContext
from activity.Main.MainRenderedData import MainRenderedData
from activity.Main.MainDomainData import MainDomainData

__author__ = 'morientes'


class MainActivity(AbstractActivity):

    activities = None

    def __init__(self):
        super(AbstractActivity, self).__init__()
        self.activities = [UC1Activity()]
        self.domain_data = MainDomainData()

    def get_activity(self, context):
        return self.activities[0]

    def transform(self, context):
        #TODO:10-05-14:morientes - este mi nie je jasne ako budeme rozoberat context preto iba po svojom
        #       vyberam suradnice x, y a akciu
        return MainActivityContext(context.x, context.y, context.action)

    def on_proccess(self, context):
        print('--- Proccess [MainActivity] ---')
        print(context)

        self.domain_data.invalidate()

    def render(self, data):
        #TODO:12-5-14:morientes - implementovat. Zatial len provizorne tranformovanie dat
        #NOTE:12-5-14:morientes - Tu mi nie je jasne ako sa premnia domenove data na render data !!!
        main_rendered_data = MainRenderedData()
        return main_rendered_data
