import unittest
from src.app_decider import app_decider
from src.task import Task

class TestApp(unittest.TestCase):

    def setUp(self):
        self.wash_dishes = Task('wash dishes', 5)
        self.cook_dinner = Task('cook dinner', 30)
        self.clean_windows = Task('clean windows', 20)

    def test_washdishes_over_cookdinner(self):
        self.assertEqual("wash dishes", app_decider(self.wash_dishes, self.cook_dinner))

    def test_cookdinner_over_washdishes(self):
        self.assertEqual("wash dishes", app_decider(self.cook_dinner, self.wash_dishes))

    def test_cookdinner_over_cleanwindows(self):
        self.assertEqual("cook dinner", app_decider(self.clean_windows, self.cook_dinner))

    def test_cleanwindows_over_cookdinner(self):
        self.assertEqual("cook dinner", app_decider(self.cook_dinner, self.clean_windows))

    def test_cleanwindows_over_washdishes(self):
        self.assertEqual("clean windows", app_decider(self.clean_windows, self.wash_dishes))

    def test_cleanwindows_over_washdishes(self):
        self.assertEqual("clean windows", app_decider(self.wash_dishes, self.clean_windows))