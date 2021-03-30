# API for postcode.io
import requests

url = "http://api.postcodes.io/postcodes/"

postcode = "e147le"

url_arg = url + postcode

print(url_arg)

response = requests.get(url_arg)

print(response.status_code)
print("\n")
# print(response.content)
# print("\n")
# print(response.headers + "\n")
# print("\n")
# print(response.history + "\n")
# print("\n")
# print(response.encoding.isdigit() + "\n")

# print(response.headers.keys())

# response.dict = response.json()
response_dict = response.json()
response_keys = response_dict["result"]

# print(type(response.dict))
# print(response.dict)

for key, _ in response_keys.items():
	if key == "postcode":
		print(f"your postcode is {response_keys[key]}")

	if key == "latitude":
		print(f"your latitude is {response_keys[key]}")

