import requests

class BlueLib:
    def __init__(self, apikey=None, base_url=None):
        self.apikey = apikey
        self.base_url = base_url
        self.headers = {}
        if self.apikey is not None:
            self.headers['token'] = self.apikey
    
    def get_recommended(self, ignore=None):
        if ignore is None:
            ignore = []
        if self.apikey is None:
            raise PermissionError("No API key was provided")
        r = requests.get(self.base_url + "/api/live/recommended", headers={**self.headers, **{"ignore": " ".join(ignore)}})
        if r.status_code != 200:
            raise ValueError(r.text)
        return r.json()

    def login(self, username, password, save=True):
        r = requests.get(self.base_url + "/api/live/login", headers={"username": username, "password": password})
        if r.status_code != 200:
            raise ValueError(r.text)
        token = r.text
        if save:
            self.apikey = token
            self.headers["token"] = token
        return token

    def register(self, username, password, save=True):
        r = requests.get(self.base_url + "/api/live/register", headers={"username": username, "password": password})
        if r.status_code != 200:
            raise ValueError(r.text)
        token = r.text
        if save:
            self.apikey = token
            self.headers["token"] = token
        return token

    def upload(self, filename, description, series=""):
        data = {
            "description": description,
            "series": series,
        }
        r = requests.get(self.base_url + "/api/live/upload", headers=self.headers, files={"video_upload": (filename, open(filename, "rb"))}, data=data)
        if r.status_code != 200:
            raise ValueError(r.text)
        return r.json()
