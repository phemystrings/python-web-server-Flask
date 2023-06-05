import json
from uuid import uuid4


class DB():
    def __init__(self, file='user.json'):
        self.file = file

    def read(self):
        with open(self.file, 'r') as user:
            return json.loads(user.read())

    def update(self, newData):
        with open(self.file, 'w') as newFile:
            newFile.write(json.dumps(newData))
            newFile.close()

    def create(self, formData):
        formData['id'] = uuid4().hex
        reader = self.read()
        reader.append(formData)
        self.update(reader)
