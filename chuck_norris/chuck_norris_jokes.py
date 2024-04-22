'''
This module gets a randomjoke from api.chucknorris.io
You may pass a name and category parameter for customization
'''
import requests
import json



def chuckjoke(**kwargs):
    '''
    Just the function that calls a random joke
    '''

    url = "https://api.chucknorris.io/jokes/random"
    name = kwargs.get('name',None)
    category = kwargs.get('category',None)

    if name !=None:
        url=f"{url}?name={name}"
    
    if category !=None:
        url=f"{url}&category={category}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)

    return(response_json['value'])

if __name__=='__main__':
    print(chuckjoke())
