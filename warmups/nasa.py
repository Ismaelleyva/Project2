#make http requests
import requests
url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2018-10-15&end_date=2018-10-23&api_key=6iEWZ7RYlmZ2XGj56Q38GiymIDVkG61WlrSR7SLn'
#API call
data = requests.get(url)
print(url)
