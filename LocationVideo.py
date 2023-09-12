from datetime import datetime
import json

class LocationVideo:
    
    def __init__(self, nameJsonVideo):
        self.nameJsonVideo = nameJsonVideo
        self.dictionaryLocation = {}

    def formatJson(self):
        f = open(self.nameJsonVideo)

        data = json.load(f)
        
        first = datetime.fromisoformat(data['1']['streams']['GPS5']['samples'][0]['date'])

        for i in data['1']['streams']['GPS5']['samples']:
            self.dictionaryLocation[(datetime.fromisoformat(i['date']) - first).seconds] = {"latitude":i['value'][0], "longitude":i['value'][1]}
        
        f.close()

    # Função que detecta o tempo
    def getLocation(self, time):
        return self.dictionaryLocation[get_sec(time)]
    

def get_sec(time):
        """Get seconds from time."""
        h, m, s = time.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)


