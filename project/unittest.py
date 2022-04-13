import unittest
from create_task import *

class TestTask(unittest.TestCase):

    def task_name_test(self):
        qe = self.assertEqual(Task("Taskname123"), "Taskname123")

        #task_name:str, task_category:int, task_time:int, task_importance:int

if __name__ == '__main__':
    unittest.main()