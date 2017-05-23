import requests


class OpenTableClient:
    base_url = "https://opentable.herokuapp.com/api"

    def __init__(self):
        pass

    @staticmethod
    def get_summary_statistics():
        r = requests.get(url="{base_url}/stats".format(base_url=OpenTableClient.base_url))

        r.raise_for_status()

        return r.json()

    @staticmethod
    def get_cities():
        r = requests.get(url="{base_url}/cities".format(base_url=OpenTableClient.base_url))

        r.raise_for_status()

        return r.json()
