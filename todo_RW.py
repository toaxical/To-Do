
import json

saveFile = 'tasks.json' # truly a variable file name, since u can modify it to your content (beware tho)

def loadTasks(saveFile):

    with open(saveFile, 'r') as readfile:
        try:
            return json.load(readfile)
        except FileNotFoundError:
            print(f"⚠️ | Please make sure the file {saveFile} exists!")
            return []
        except Exception as excptn:
            print(f"An error occurred while trying to load tasks: {excptn}")
            return []
        
def modifyTasks(tasks_data):
    with open(saveFile, 'w') as mdfile:
        try:
            json.dump(tasks_data, mdfile, indent=4)
        except Exception as excptn:
            print(f"Error occurred while saving tasks! : {excptn}")
        else:
            print("✅ | Success!")

