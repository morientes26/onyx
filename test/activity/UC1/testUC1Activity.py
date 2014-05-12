import unittest
from activity.UC1.UC1ActivityContext import UC1ActivityContext
from activity.UC1.UC1Activity import UC1Activity
from input.ui_driver.UIContext import UIContext

__author__ = 'morientes'


class TestUC1Activity(unittest.TestCase):

    ui_context = None
    uc1_activity = None

    def setUp(self):
        """
        Method start before a test case
        """
        self.ui_context = UIContext("onClick", 12, 32, "UC1")
        self.uc1_activity = UC1Activity()
        pass

    def tearDown(self):
        """
        Method start after a test case
        """
        pass

    def test_init(self):
        self.assertEqual(self.uc1_activity.activities, None)

    def test_transform(self):
        self.assertIsInstance(self.uc1_activity.transform(self.ui_context), UC1ActivityContext)

    def test_get_activity(self):
        self.assertEqual(self.uc1_activity.get_activity(self.ui_context), None)

    def test_proccess(self):
        self.uc1_activity.proccess(self.ui_context)

if __name__ == '__main__':
    unittest.main()