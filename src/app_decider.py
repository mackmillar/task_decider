def app_decider(task1, task2):
    
    
    if task1.description == "wash dishes" and task2.description == "cook dinner" or task1.description == "cook dinner" and task2.description == "wash dishes":
        return 'wash dishes'
    elif task1.description == 'clean windows' and task2.description == 'cook dinner' or task1.description == 'cook dinner' and task2.description == 'clean windows' :
        return 'cook dinner'
    elif task1.description == 'clean windows' and task2.description == 'wash dishes' or task1.description == 'wash dishes' and task2.description == 'clean windows' :
        return "clean windows"


