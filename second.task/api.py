import requests
# response = requests.get('https://restcountries.com/v3.1/all') 
# r = response.text 
response = requests.get('https://restcountries.com/v3.1/all') 
text = response.json()
text = text[0]
text = text["name"]
text = text["common"]
print(text)


