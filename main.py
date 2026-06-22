import FreeSimpleGUI as gui
import Backend
import time

ls = Backend.ToDos

gui.theme('DarkTeal12')

clock = gui.Text(
    time.strftime("%H:%M:%S", time.localtime()),
    key='clock'
)

textbox = gui.InputText(
    tooltip='just text',
    key='todo'
)

label = gui.Text("How can I help you?")

addbt = gui.Button("add")

list_box = gui.Listbox(
    ls,
    size=[40, 10],
    key='todos',
    enable_events=True
)

editbt = gui.Button("edit")

exitbt = gui.Button("Exit")

deletebtt = gui.Button("delete")

window = gui.Window(
    "Home page",
    layout=[
        [clock],
        [label],
        [textbox, addbt],
        [list_box,editbt, deletebtt],
        [exitbt]
    ],
    font=("Arial", 13)
)

while True:

    event, values = window.read(timeout=200)

    window['clock'].update(
        time.strftime("%H:%M:%S", time.localtime())
    )

    match event:

        case "add":

            task = values['todo'].strip()

            if not task:
                gui.popup("Enter a task")

                continue

            result = Backend.add_todo(task)

            if not result:
                gui.popup("Task already exists")

            list_box.update(ls)

            window['todo'].update(value='')
        case "edit":

            if not values['todos']:
                gui.popup("Select a task")

                continue

            old_task = values['todos'][0]

            new_task = values['todo'].strip()

            if not new_task:
                gui.popup("Enter edited task")

                continue

            if old_task == new_task:
                gui.popup("No changes made")

                continue

            result = Backend.edit_todo(old_task, new_task)

            if not result:
                gui.popup("Edit failed")

                continue

            list_box.update(ls)

            window['todo'].update(value='')

        case "delete":

            if not values['todos']:
                gui.popup("Select a task")

                continue

            del_task = values['todos'][0]

            result = Backend.del_todo(del_task)

            if not result:
                gui.popup("Delete failed")

                continue

            list_box.update(ls)

            window['todo'].update(value='')
        case "todos":

            if values['todos']:

                window['todo'].update(
                    value=values['todos'][0]
                )

        case "Exit":

            Backend.out()

            break

        case gui.WINDOW_CLOSED:

            Backend.out()

            break

window.close()