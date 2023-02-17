FILEPATH = 'todos.txt' #I had to put the folder too


def get_todos(filepath=FILEPATH):
    """ Read the text and return the list of to do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """"Write the todo item in the file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
