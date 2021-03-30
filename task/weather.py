import requests

class Weather():
    def __init__(self):
        self._greetings()
        self.city = self._askdata()
        self.response = self.status_code_check()


    def _greetings(self):
        print("Hello user! Welcome to the weather script!")

    def _askdata(self):
        city = input("Please insert the city for which you'd like to check the weather: ").lower()
        return city

    def status_code_check(self):
        try:
            responses = requests.get('http://api.openweathermap.org/data/2.5/weather?p='+ self.city
                +'&APPID=****************************8&units=metric')

            if responses.status_code == 200:
                print("the website is up and running!\n")

                print(responses.json())
                return responses.json()
            else:
                print("Oops, something went wrong! status code: " + str(responses.status_code))
                raise("Shutting down")
        except:
            raise Exception("Oops, something went wrong. Call your neighbourhood programmer!")

if __name__=='__main__':
    obj = Weather()

