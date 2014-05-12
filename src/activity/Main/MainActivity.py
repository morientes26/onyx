from Activity.AbstractActivity import AbstractActivity
from Activity.UC1.UC1Activity import UC1Activity
from Context.Main.MainActivityContext import MainActivityContext


class MainActivity(AbstractActivity):

    activities = None

    def __init__(self):
        super(AbstractActivity, self).__init__()
        #NOTE:10-05-14:morientes - neviem ci som spravne pochopil pridavanie aktivit do listu aktivit
        #       a ci sa to takto v kazdej aktivite bude nastavovat napevno v konstruktore
        self.activities = [UC1Activity()]

    def get_activity(self, context):
        return self.activities[0]

    def transform(self, context):
        #TODO:10-05-14:morientes - este mi nie je jasne ako budeme rozoberat context preto iba po svojom
        #       vyberam suradnice x, y a akciu
        return MainActivityContext(context.x, context.y, context.action)

    def on_proccess(self, context):
        print('--- Proccess [MainActivity] ---')
        print(context)
