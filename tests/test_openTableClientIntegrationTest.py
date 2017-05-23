from unittest import TestCase

from opentable.client import OpenTableClient


class OpenTableClientIntegrationTest(TestCase):
    def test_fetching_summary_statistics(self):
        summary_statistics = OpenTableClient.get_summary_statistics()
        self.assertIsNotNone(summary_statistics)
        self.assertEqual(len(summary_statistics), 3)
        self.assertTrue("countries" in summary_statistics)
        self.assertTrue("cities" in summary_statistics)
        self.assertTrue("restaurants" in summary_statistics)

    def test_fetching_cities(self):
        cities = OpenTableClient.get_cities()
        self.assertIsNotNone(cities)
        self.assertEqual(len(cities), 2)
        self.assertTrue("count" in cities)
        self.assertTrue("cities" in cities)
