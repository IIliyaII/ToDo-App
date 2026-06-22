import csvwr
import welcomesound
import os

if not os.path.exists('build/data.csv'):
    with open('build/data.csv', 'w', newline='', encoding='utf-8'):
        pass

ToDos = []
welcomesound.welcomesound()

csvwr.listadd('build/data.csv', ToDos)


def add_todo(todo):

    todo = todo.strip()

    if not todo:
        return False

    if todo not in ToDos:

        ToDos.append(todo)

        csvwr.writer('build/data.csv', ToDos)

        return True

    return False


def edit_todo(old_task, new_task):

    new_task = new_task.strip()

    if not new_task:
        return False

    if old_task not in ToDos:
        return False

    idx = ToDos.index(old_task)

    ToDos[idx] = new_task

    csvwr.writer('build/data.csv', ToDos)

    return True


def del_todo(task):

    if task in ToDos:

        ToDos.remove(task)

        csvwr.writer('build/data.csv', ToDos)

        return True

    return False


def out():
    welcomesound.byesound()