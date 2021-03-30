# Task
- greeting user
- ask user to input data
- validate connection
- create class
- check status code
- check weather

### Solution
```python
import requests, json
# weather curtesy of openweathermap.org

class Weather():
    # the init method also runs our program in order
    def __init__(self):
        self._greetings() # we greet the user
        self.city = self._askdata() # we ask the user to choose a city in GB
        self.city_id = self._city_id(self.city) # this is here because the api requires custom city codes
        self.response = self._status_code_check() # checks if the response went well and fetches the output
        self._tell_weather() # prints the current weather in the chosen city


    def _greetings(self):
        print("Hello user! Welcome to the weather script!")

    def _city_id(self, city_name):
        with open("city_list.json", "r") as file: # the list of cities and relative IDs is kept in this file
            for city in file: # we look for the chosen city in the list
                if city["name"] == city_name:
                    return city["id"] # then we return the ID

    def _askdata(self): # taking input from user
        city = input("Please insert the city in GB for which you'd like to check the weather: ")
        # formatting the input
        city = city.lower()
        city = city.capitalize()
        
        return city

    def _status_code_check(self):
        try:
            # we try to get a valid webpage for the selected city (with city ID)
            responses = requests.get('http://api.openweathermap.org/data/2.5/weather?id='+ self.city_id
                +'&appid=********************************')

            if responses.status_code == 200: # if the page exists and works fine
                print("the website is up and running!\n")

                return responses.json() # return the contents of the page as a dict

            else: # otherwise we warn the user and stop the execution
                print("Oops, something went wrong! status code: " + str(responses.status_code))

                raise Exception("Shutting down")
        
        except: # if we don't get any kind of response, we stop the execution
            raise Exception("Oops, something went wrong. Call your neighbourhood programmer!")

    def _tell_weather(self): # finally, we tell the weather to the user
        for key, value in self.response.items():

            if key == "weather":
                for jey, jalue in value[0].items():
            
                    if jey == "description":
                        print(f"the weather in {self.city} right now is '{jalue}'!")



if __name__=='__main__': # only when executing this file
    obj = Weather() # run the init
```