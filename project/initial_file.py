#####################
#                   #
#   TASK MANAGER    #
#       v.1         #
#                   #
#####################

from create_task import Task

# Password check for a file

# Import a file, initial setup

while(True):

    instructions = "Choose an option:\n\t1 Create a new task\n"
    choice = input(instructions)

    if choice == "1":

        # these cateogires could be later changed by the user
        categories = ["Home", "School", "Work", "Personal", "Other"]

        task_t = str(input("What is the task about: "))

        print("Choose the number of the most fitting category: ")
        for cate in categories:
            print(categories.index(cate)+1, cate) # Formatting?
        task_cate = int(input("")) # Error handling missing

        task_time = int(input("How long will the task take (minutes): ")) # Error handling missing
        task_imp = int(input("How long importat is the task (1-5): ")) # Error handling missing

        newtask = Task(task_t, task_cate, task_time, task_imp)

        print("Created a new task:\n", newtask)
        
        # save the task here?


    # Read the file - in a nice way
    # Check not started / in progress / done tasks

    # Add a task to the file
    # Default values if string empty?

    # Make task in progress
    # Make task in done - add TIME SPENT

    # SETTINGS
    # Check task categories
    # Chek subclass categories


    # Import task list based on importance and time estimated
    else:
        print("The choice is invalid. Please try again!")
