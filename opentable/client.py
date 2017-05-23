import requests


class OpenTableClient:
    def __init__(self):
        self.base_url = "https://opentable.herokuapp.com/api"

    def get_summary_statistics(self):
        r = requests.get(url="{base_url}/stats".format(base_url=self.base_url))

        r.raise_for_status()

        r.json()

    def get_cities(self):
        r = requests.get(url="{base_url}/cities".format(base_url=self.base_url))

        r.raise_for_status()

        r.json()
