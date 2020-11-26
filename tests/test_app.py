import unittest
from src.app_decider import app_decider
from src.task import Task

class TestApp(unittest.TestCase):

    def setUp(self):
        self.wash_dishes = Task('wash the dishes', 5)
        self.cook_dinner = Task('make some tasty food', 30)
        self.clean_windows = Task('make them transparent', 20)

    def test_washdishes_over_cookdinner(self):
        self.assertEqual("wash dishes", app_decider(self.wash_dishes, self.cook_dinner))