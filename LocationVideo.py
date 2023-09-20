import dateutil.parser
import json
import os
class LocationVideo:

    def __init__(self, nameJsonVideo):
        self.nameJsonVideo = nameJsonVideo
        self.dictionaryLocation = {}

    def formatJson(self):
        f =  open(os.path.dirname(os.path.realpath(__file__)) + '\\json\\' + self.nameJsonVideo + '.json')

        data = json.load(f)

        first = dateutil.parser.isoparse(data['1']['streams']['GPS5']['samples'][0]['date'])

        for i in data['1']['streams']['GPS5']['samples']:
            self.dictionaryLocation[(dateutil.parser.isoparse(i['date']) - first).seconds] = {"latitude":i['value'][0], "longitude":i['value'][1]}

        f.close()

    # Função que detecta o tempo
    def getLocation(self, time):
        second = get_sec(time)
        if(second < len(self.dictionaryLocation)):
            return self.dictionaryLocation[second]

    def getLocationBySecond(self, second):
        if(second < len(self.dictionaryLocation)):
            return self.dictionaryLocation[second]

def get_sec(time):
        """Get seconds from time."""
        h, m, s = time.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)