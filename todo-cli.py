
__version__  = '1.1.0'

import datetime
import todo_RW as savescr


def greet():
    if datetime.datetime.now().time().strftime('%p') == 'AM':
        print('Ohayo! Have a good morning! 😊')

    elif datetime.datetime.now().time().strftime('%p') == 'PM':
        print('Konichiwa! Have a good day! 😊')


def addTask(tasks):
    adding = True
    while adding:
        task = input("Type out your task! (type 'b' or 'back' to go back) \n> ")

        if task == 'b' or task == 'exit' or task == 'back':
            adding = False
            return
        else:
            lastid = tasks[-1].get('id')
            tasks.append({'id': lastid+1, 'task': task})
            print('⸜(｡˃ ᵕ ˂ )⸝♡\n')
    
    return tasks


def viewTasks(tasks):

    imlooking = True

    while imlooking:
        print('\n⊹₊ ˚‧︵‿₊୨ ~ TASKS ~ ୧₊‿︵‧ ˚ ₊⊹\n')

        x=1
        for items in tasks:

            for slno in range(x, x+1):
                item = f"{slno}. {items.get('task')}"
                x+=1
                print(item)
        
        if len(tasks) == 0:
            print('\n woah.. so empty... 🍃\n')
            print('     ｡☆✼★━━━━━━━━━━━━★✼☆｡')
            break

        print('\n     ｡☆✼★━━━━━━━━━━━━★✼☆｡')

        cont = input("\n['b' to go back]\n")
        if cont == 'b' or cont == 'exit' or cont == 'back':
            imlooking = False
    return


def removeTask(tasks):
    print('⊹₊ ˚‧︵‿₊୨ ~ REMOVE TASKS ~ ୧₊‿︵‧ ˚ ₊⊹')

    imremoving = True

    if len(tasks) < 1:
        print("\n🤔  | There aren't any tasks to begin removing from!")
        return

    while imremoving:
        print()

        x = 1
        for items in tasks:
            for slno in range(x, x+1):
                item = f"{slno}. {items.get('task')} [ID: {items.get('id')}]"
                x += 1
                print(item)

        remId = input("\nEnter the 'ID' of the task you'd like to remove ('b' to go back): >  ")
        try:
            remId = int(remId)
        except ValueError:
            if remId == 'b' or remId == 'back':
                break
            else:
                print("⸝🦋 | Um.. I can't find a task with that Id! :C \n")

        else:
            try:
                tempRemlist = []
                for task in tasks:
                    if task["id"] == remId:
                        tempRemlist.append(task)
                        break 

                remTask_indx = tasks.index(tempRemlist[0])
                tasks.pop(remTask_indx)
    
            except:
                IndexError()
                print('⚠️ | Sorry, that task does not exist.\n')
    return tasks


def main():


    tasks = savescr.loadTasks('./tasks.json')  # head to todo_RW.py and edit the 'tasks.json' if you want to save tasks in a different file, though IT SHOULD BE A JSON FILE!

    inApp = True
    while inApp:
            try:
                print('\n⊹₊ ˚‧︵‿₊୨ ~ To-Do List ~ ୧₊‿︵‧ ˚ ₊⊹')
                initi = int(input("\n1. Add Task \n2. View Tasks \n3. Remove a Task \n4. Exit \n> "))
            except:
                ValueError()
                print('⚠️  | Invalid input!')
            else:
                if initi == 1:
                    addTask(tasks)
                    savescr.modifyTasks(tasks)
                elif initi == 2:
                    viewTasks(tasks)
                elif initi == 3:
                    removeTask(tasks)
                    savescr.modifyTasks(tasks)
                elif initi == 4:
                    print('\nヾ( ˃ᴗ˂ )◞ • *✰ bye bye!\n')
                    inApp = False

if __name__ == '__main__':
    print(f"\x1B[3mTo-Do List v{__version__}\x1B[0m")
    greet()
    main()