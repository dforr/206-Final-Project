
#Deezer API
import requests 
import json 
#base_url = 'https://api.deezer.com/version/service/id/method/?parameters'

response = requests.get("https://api.deezer.com/chart/artists") #go get info from URL and package info and put it into response object
print(response.json()) #print(response.status_code) #get status code classdeezer.client.Client(app_id=None, app_secret=None, access_token=None, headers=None, **kwargs)
text = json.loads(response.text) #convert to dictionary 
artists = text.get('artists')
data = artists.get('data')
print(data)
for info in data: 
    name = info['name']
    rank = info['position']
    print(name)
    print(rank)

    '''
import requests
url = "https://billboard-api2.p.rapidapi.com/artist-100"
querystring = {"date":"2019-05-11","range":"1-25"}
headers = {
    'x-rapidapi-key': "e8987c562amsh78b1a8d73318a6fp16a5aajsn465e38986a0e",
    'x-rapidapi-host': "billboard-api2.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
'''
    