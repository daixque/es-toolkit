import requests
import json

class RestClient:
    def __init__(self, base_url, *, api_key=None):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'Authorization': f'ApiKey {api_key}' if api_key else None,
        }

    def handle_error(self, response):
        if response.status_code >= 500:
            print('Error from server:')
            print(response.json())
            exit(1)
        if response.status_code >= 400:
            print('Error:')
            print(response.json())


    def get(self, path):
        response = requests.get(self.base_url + path, headers=self.headers)
        print(f'GET {path}: {response.status_code}')
        self.handle_error(response)
        return response
    
    def post(self, path, *, data={}, file=None):
        if file:
            # read json from file
            with open(file) as f:
                data = json.load(f)
        response = requests.post(self.base_url + path, json=data, headers=self.headers)
        print(f'POST {path}: {response.status_code}')
        self.handle_error(response)
        return response
    
    def put(self, path, *, data={}, file=None):
        if file:
            # read json from file
            with open(file) as f:
                data = json.load(f)
        response = requests.put(self.base_url + path, json=data, headers=self.headers)
        print(f'PUT {path}: {response.status_code}')
        self.handle_error(response)
        return response
    
    def put_if_not_exists(self, path, *, data={}, file=None):
        if self.exists(path):
            print(f'Skip: {path} already exists') 
            return None
        return self.put(path, data=data, file=file)
    
    def delete(self, path):
        response = requests.delete(self.base_url + path, headers=self.headers)
        print(f'DELETE {path}: {response.status_code}')
        self.handle_error(response)
        return response
    
    def head(self, path):
        response = requests.head(self.base_url + path, headers=self.headers)
        print(f'HEAD {path}: {response.status_code}')
        self.handle_error(response)
        return response
    
    def exists(self, path):
        response = requests.get(self.base_url + path, headers=self.headers)
        return response.status_code == 200
