import unittest
from create_task import *

class TestTask(unittest.TestCase):

    def test_task_name(self):
        print("Test starting")

        tasknames = []

        for i in range(3):
            taskname = "Taskname" + str(i)
            tasknames.append(taskname)

        t1 = Task(tasknames[1])

        print(t1)




    #Task(task_t, task_cate, task_time, task_imp)
        

if __name__ == '__main__':
    unittest.main()