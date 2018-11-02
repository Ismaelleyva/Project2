api_token = '6iEWZ7RYlmZ2XGj56Q38GiymIDVkG61WlrSR7SLn'
url= "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&"
for api_token in url:
    print(url+api_token)
