import requests, json

class Weather():
    def __init__(self):
        self._greetings()
        self.city = self._askdata()
        self.city_id = self._city_id(self.city)
        self.response = self._status_code_check()
        self._tell_weather()


    def _greetings(self):
        print("Hello user! Welcome to the weather script!")

    def _city_id(self, city_name):
        with open("city_list.json", "r") as file:
            for city in file:
                if city["name"] == city_name:
                    return city["id"]

    def _askdata(self):
        city = input("Please insert the city for which you'd like to check the weather: ")
        city = city.lower()
        city = city.capitalize()
        
        return city

    def _status_code_check(self):
        try:
            responses = requests.get('http://api.openweathermap.org/data/2.5/weather?id='+ self.city_id
                +'&appid=********************************')

            if responses.status_code == 200:
                print("the website is up and running!\n")

                return responses.json()
            else:
                print("Oops, something went wrong! status code: " + str(responses.status_code))
                raise("Shutting down")
        except:
            raise Exception("Oops, something went wrong. Call your neighbourhood programmer!")

    def _tell_weather(self):
        for key, value in self.response.items():
            if key == "weather":
                for jey, jalue in value[0].items():
                    if jey == "description":
                        print(f"the weather in {self.city} right now is '{jalue}'!")





if __name__=='__main__':
    obj = Weather()

