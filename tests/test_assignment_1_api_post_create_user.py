import requests
import json


url = 'https://reqres.in/api/users'

data = {
    'name': 'Rendy',
    'job': 'QA Engineer'
}

response = requests.post(url, json=data)
if response.status_code == 201:
    print('POST request successful!')
    print('Response data:')
    print(response.json()) 
else:
    print(f'POST request failed with status code: {response.status_code}')
