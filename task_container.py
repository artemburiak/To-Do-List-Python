import json

class Task_container:
    def __init__(self):
        self.tasks = []
        try:
            self.load()
        except:
            pass

    def addtask(self, text, text2):
        data = {
            "text": text, 
            "text2": text2
        }
        self.tasks.append(data)
        print(data)

    def gettasks(self):
        return self.tasks

    def save(self):
        data = json.dumps(self.tasks)
        file = open('file.txt', 'w')
        file.write(data)
        file.close()

    def load(self):
        file = open('file.txt', 'r')
        data = file.read()
        file.close()
        if len(data) != 0:
            self.tasks = json.loads(data)

    def deltask(self, title, text):
        newlist = []
        for i in self.tasks:
            if i['text'] == title and i['text2'] == text:
                pass
            else:
                newlist.append(i)
        self.tasks = newlist
        self.save()




