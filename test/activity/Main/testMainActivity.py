import unittest
from Activity.Main.MainActivity import MainActivity
from Context.Main.MainActivityContext import MainActivityContext
from Activity.UC1.UC1Activity import UC1Activity
from Context.UIContext import UIContext


class TestMainActivity(unittest.TestCase):

    ui_context = None
    main_activity = None

    def setUp(self):
        """
        Method start before a test case
        """
        self.ui_context = UIContext("onClick", 12, 32, "UC1")
        self.main_activity = MainActivity()
        pass

    def tearDown(self):
        """
        Method start after a test case
        """
        pass

    def test_init(self):
        self.assertNotEquals(self.main_activity.activities.__len__(), 0)
        self.assertIsInstance(self.main_activity.activities[0], UC1Activity)

    def test_transform(self):
        self.assertIsInstance(self.main_activity.transform(self.ui_context), MainActivityContext)

    def test_get_activity(self):
        self.assertIsInstance(self.main_activity.get_activity(self.ui_context), UC1Activity)

    def test_proccess(self):
        self.main_activity.proccess(self.ui_context)

if __name__ == '__main__':
    unittest.main()