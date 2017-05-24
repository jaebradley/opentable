from unittest import TestCase

from opentable.client import OpenTableClient
from opentable.queries import RestaurantSearchQuery
from opentable.queries.query_parameters import PerPage, PriceRange


class OpenTableClientIntegrationTest(TestCase):
    client = OpenTableClient()

    def test_fetching_summary_statistics(self):
        summary_statistics = self.client.get_summary_statistics()
        self.assertIsNotNone(summary_statistics)
        self.assertEqual(len(summary_statistics), 3)
        self.assertTrue("countries" in summary_statistics)
        self.assertTrue("cities" in summary_statistics)
        self.assertTrue("restaurants" in summary_statistics)

    def test_fetching_cities(self):
        cities = self.client.get_cities()
        self.assertIsNotNone(cities)
        self.assertEqual(len(cities), 2)
        self.assertTrue("count" in cities)
        self.assertTrue("cities" in cities)

    def test_fetching_restaurants(self):
        query = RestaurantSearchQuery(price_range=PriceRange.two_dollars, state_code="MA", per_page=PerPage.ten)
        restaurants = self.client.search_restaurants(query=query)
        self.assertIsNotNone(restaurants)
        self.assertEqual(len(restaurants), 4)
        self.assertTrue("current_page" in restaurants)
        self.assertTrue("per_page" in restaurants)
        self.assertTrue("restaurants" in restaurants)
        self.assertTrue("total_entries" in restaurants)

        first_restaurant = restaurants["restaurants"][0]
        self.assertIsNotNone(first_restaurant)
        self.assertTrue("id" in first_restaurant)
        self.assertTrue("name" in first_restaurant)
        self.assertTrue("city" in first_restaurant)
        self.assertTrue("state" in first_restaurant)
        self.assertTrue("area" in first_restaurant)
        self.assertTrue("postal_code" in first_restaurant)
        self.assertTrue("country" in first_restaurant)
        self.assertTrue("phone" in first_restaurant)
        self.assertTrue("lat" in first_restaurant)
        self.assertTrue("lng" in first_restaurant)
        self.assertTrue("price" in first_restaurant)
        self.assertTrue("reserve_url" in first_restaurant)
        self.assertTrue("mobile_reserve_url" in first_restaurant)
        self.assertTrue("image_url" in first_restaurant)
