import itertools

class Task:

    def __init__(self, task_name:str, task_category:int=1, task_time:int=0, task_importance:int=1):
        
        self.task_id = id_creator()

        self.task_name = task_name
        self.task_category = task_category
        self.task_time = task_time
        self.time_spent = 0
        self.task_importance = task_importance # 1-5, 5 most important

        self.task_status = 0 # 0 = not started, 1 = in progress, 2 = finished

    def __str__(self):

        # Category

        # Status
        tulos = ""
        if self.task_status == 0:
            tulos = "Not started"
        elif self.task_status == 1:
            tulos = "In progress"
        elif self.task_status == 2:
            tulos = "Finished"

        return f"{self.task_id}: {self.task_name} from the category {self.task_category}. Time {self.time_spent}/{self.task_time}. Status: {tulos}"


class id_creator:
    id_iter = itertools.count()

    def __init__(self):
        self.id = next(id_creator.id_iter)

    def __str__(self):
        return f"{self.id}"