
__version__  = '1.0.0'

import datetime


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
            tasks.append(task)            
            print("✅ | Added!\n")

    return tasks


def viewTasks(tasks):

    imlooking = True

    while imlooking:
        print('\n⊹₊ ˚‧︵‿₊୨ ~ TASKS ~ ୧₊‿︵‧ ˚ ₊⊹\n')

        for x in tasks:
            print(f'{1+tasks.index(x)}. '+x)
        
        if len(tasks) == 0:
            print('\n woah.. so empty... 🍃\n')
            print('     ｡☆✼★━━━━━━━━━━━━★✼☆｡')
            break

        print('     ｡☆✼★━━━━━━━━━━━━★✼☆｡')

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
        for x in tasks:
            print(f'{1+tasks.index(x)}. '+x)

        indx = input("\nEnter the 'number' of the task you'd like to remove ('b' to go back): >  ")
        try:
            indx = int(indx)
        except:
            TypeError()
            break
        else:
            try:
                print(f'Sucessfully removed {tasks[indx-1]} from tasks.')
                tasks.pop(indx-1)
            except:
                IndexError()
                print('⚠️ | Sorry, that task does not exist.\n')
            else:
                continue
    return tasks


def main():
    tasks = []

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
                elif initi == 2:
                    viewTasks(tasks)
                elif initi == 3:
                    removeTask(tasks)
                elif initi == 4:
                    inApp = False

if __name__ == '__main__':
    print(f"\x1B[3mTo-Do List v{__version__}\x1B[0m")
    greet()
    main()