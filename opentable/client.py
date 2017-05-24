import requests

from opentable.queries.query_builders import RestaurantSearchQueryParametersBuilder


class OpenTableClient:
    base_url = "https://opentable.herokuapp.com/api"

    def __init__(self):
        self.restaurant_search_query_parameters_builder = RestaurantSearchQueryParametersBuilder()

    def get_summary_statistics(self):
        r = requests.get(url="{base_url}/stats".format(base_url=OpenTableClient.base_url))

        r.raise_for_status()

        return r.json()

    def get_cities(self):
        r = requests.get(url="{base_url}/cities".format(base_url=OpenTableClient.base_url))

        r.raise_for_status()

        return r.json()

    def search_restaurants(self, query):
        r = requests.get(url="{base_url}/restaurants".format(base_url=OpenTableClient.base_url),
                         params=self.restaurant_search_query_parameters_builder.build_query_parameters(query=query))

        r.raise_for_status()

        return r.json()

