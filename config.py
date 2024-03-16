import json
from os.path import exists
from os import mkdir

class Config:
    def __init__(self):
        if not exists('./src'):
            mkdir('./src')
        if exists('./src/config.json'):
            with open('./src/config.json', 'r') as openfile:
                data = json.load(openfile)
        else:
            config = {
                'chatId': None,
                'isFirstLaunch':True,
                'writableToChat':False,
                'queueSencitivity':0.9,
                'inQueueSensitivity':0.7
            }
            with open('./src/config.json', 'w') as outfile:
                jsonObject = json.dumps(config)
                outfile.write(jsonObject)
        with open('./src/config.json', 'r') as openfile:
                data = json.load(openfile)
        self.chatId: str | None = data['chatId']
        self.isFirstLaunch: bool = data['isFirstLaunch']
        self.writableToChat: bool = data['writableToChat']
        self.queueSencitivity: float = data['queueSencitivity']
        self.inQueueSensitivity: float = data['inQueueSensitivity']
        
    def writeConfig(self):
        config = {
                'chatId': self.chatId,
                'isFirstLaunch': self.isFirstLaunch,
                'writableToChat': self.writableToChat,
                'queueSencitivity': self.queueSencitivity,
                'inQueueSensitivity': self.inQueueSensitivity
        }
        print(config)
        with open('./src/config.json', 'w') as outfile:
            jsonObject = json.dumps(config)
            outfile.write(jsonObject)

    def setData(self, chatId, queueSencitivity, inQueueSensitivity, writableToChat):
        self.chatId = chatId
        self.queueSencitivity = queueSencitivity
        self.inQueueSensitivity = inQueueSensitivity
        self.writableToChat = writableToChat
        self.writeConfig()