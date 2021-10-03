import requests

#the required first parameter of the 'get' method is the 'url':
url = 'https://w3schools.com/python/demopage.htm'
response = requests.get(url)

#print the response text (the content of the requested file):

print("Response Status Code:",response.status_code)
print("Response Body:",response.text)
print("Response Headers:",response.headers)
print("Response header keys:", response.headers.keys())
for key in response.headers.keys():
    print( key, '=' , response.headers[key] )