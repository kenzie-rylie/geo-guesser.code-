import requests
import json
import threading
import time
from json import dumps

API_KEY = "tXLFRVKRTvdA"
PROJECT_TOKEN = "toq7r-OTLXNj"
RUN_TOKEN = "t2ddTYSXTCjs"

class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.data = self.get_data()

    #getting data from the most recent run...
    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data', params=self.params)
        data = json.loads(response.text)
        return data

#stuff for getting total information...."specification" can be total/deaths/recovered
    def get_total_cases(self):
        data = self.data["total"]

        #what it is doing here is looping through all of the data to find an entry called "coronavirus cases"
        for content in data:
            if content["name"] == "Coronavirus Cases:":
                return content['value']
            return "0"


    def get_total_deaths(self):
        data = self.data["total"]

        for content in data:
            if content["name"] == "Deaths:":
                return content['value']

    def get_total_recovered(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Recovered:":
                return content['value']

#stuff for getting country specific info
    def get_country_data(self, country):
        data= self.data["country"]

        for content in data:
            if content ['name'].lower() == country.lower():
                return content

        return "0"
    def update_data(self):
        response = requests.post(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run', params=self.params)

        def poll():
            time.sleep(0.1)
            old_data = self.data
            while True:
                new_data = self.get_data()
                if new_data != old_data:
                    self.data = new_data
                    print("Data updated")
                    break
                time.sleep(5)

        t = threading.Thread(target=poll)
        t.start()

data = Data(API_KEY, PROJECT_TOKEN)

def worldtotal():
    worlddictionary = {"worldtotal": data.get_total_cases(),
                       "worlddeaths": data.get_total_deaths(),
                       "worldrecovered":data.get_total_recovered()}
    return worlddictionary


def countrydata():
    dictionary1={"brazildata": data.get_country_data("brazil")['total_cases'],
                 "brazildeaths": data.get_country_data("brazil")['total_deaths'],
                 "brazilrecovered": data.get_country_data("brazil")['total_recovered'],

                 "icelandtotal": data.get_country_data("iceland")['total_cases'],
                 "icelanddeaths": data.get_country_data("iceland")['total_deaths'],
                 "icelandrecovered": data.get_country_data("iceland")['total_recovered'],

                 "japantotal": data.get_country_data("japan")['total_cases'],
                 "japandeaths": data.get_country_data("japan")['total_deaths'],
                 "japanrecovered": data.get_country_data("japan")['total_recovered'],

                 "denmarktotal": data.get_country_data("denmark")['total_cases'],
                 "denmarkdeaths": data.get_country_data("denmark")['total_deaths'],
                 "denmarkrecovered": data.get_country_data("denmark")['total_recovered'],

                 "nigertotal": data.get_country_data("niger")['total_cases'],
                 "nigerdeaths": data.get_country_data("niger")['total_deaths'],
                 "nigerrecovered": data.get_country_data("niger")['total_recovered'],

                 "indiatotal": data.get_country_data("india")['total_cases'],
                 "indiadeaths": data.get_country_data("india")['total_deaths'],
                 "indiarecovered": data.get_country_data("india")['total_recovered'],}
    return dictionary1

