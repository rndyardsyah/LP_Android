import requests

url = 'https://reqres.in/api/users/1'


response = requests.get(url)

if response.status_code == 200:
    print('Request successful!')

    print('Response data:')
    print(response.json())
else:
    print(f'Request failed with status code: {response.status_code}')
