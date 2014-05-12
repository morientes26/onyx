from Activity.AbstractActivity import AbstractActivity
from Context.UC1.UC1ActivityContext import UC1ActivityContext


class UC1Activity(AbstractActivity):

    activities = None

    def __init__(self):
        super(AbstractActivity, self).__init__()
        self.activities = None

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
