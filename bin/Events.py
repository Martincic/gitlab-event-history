import requests
import time
from bin.Token import Token

BASE_URL = 'https://gitlab.com/api/v4/events'
TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

class Event():
    def __init__(self):
        self._baseUrl = BASE_URL
        
    def rowCount(self):
        # The length of the outer list.
        print("ROWS: "+str(len(self._data)))
        return len(self._data)

    def columnCount(self):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        print("COLUMNS: "+str(len(self._data[0])))
        return len(self._data[0])
    
    # Parse data 
    def getData(self):
        r = requests.get(BASE_URL+"?per_page=100&page=1", headers={"PRIVATE-TOKEN":Token.getToken()})
        r.raise_for_status()

        data = r.json()
        parsed_data = []
        print(data[0]['created_at'])
        for item in data:
            timestamp = time.strptime(item['created_at'], TIME_FORMAT)
            date = str(timestamp.tm_mday)+'/'+str(timestamp.tm_mon)+'/'+str(timestamp.tm_year)
            real_time = str(timestamp.tm_hour)+':'+str(timestamp.tm_min)
            
            description = item['target_title'] if item['target_title'] else item['push_data']['commit_title']
            
            parsed_data.append([
                date,
                real_time,
                item['action_name'],
                description,
            ])

        self._data = parsed_data
        return self._data

