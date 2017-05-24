from unittest import TestCase

from opentable.queries.query_builders import RestaurantSearchQueryParametersBuilder
from opentable.queries.query_parameters import PriceRange, PerPage


class MockQuery:
    def __init__(self, price_range=None, name=None, address_line=None, state_code=None, city_name=None, zip_code=None,
                 country_code=None, page=None, per_page=None):
        self.price_range = price_range
        self.name = name
        self.address_line = address_line
        self.state_code = state_code
        self.city_name = city_name
        self.zip_code = zip_code
        self.country_code = country_code
        self.page = page
        self.per_page = per_page


class TestRestaurantSearchQueryParametersBuilder(TestCase):
    parameters_builder = RestaurantSearchQueryParametersBuilder()

    def test_no_defined_parameters(self):
        query = MockQuery()
        self.assertEqual(self.parameters_builder.build(query=query), {})

    def test_defined_price_range(self):
        price_range = PriceRange.four_dollars
        query = MockQuery(price_range=price_range)
        self.assertEqual(self.parameters_builder.build(query=query), {"price": price_range.value})

    def test_defined_name(self):
        name = "name"
        query = MockQuery(name=name)
        self.assertEqual(self.parameters_builder.build(query=query), {"name": name})

    def test_defined_address_line(self):
        address_line = "address line"
        query = MockQuery(address_line=address_line)
        self.assertEqual(self.parameters_builder.build(query=query), {"address": address_line})

    def test_defined_state_code(self):
        state_code = "state code"
        query = MockQuery(state_code=state_code)
        self.assertEqual(self.parameters_builder.build(query=query), {"state": state_code.upper()})

    def test_defined_city_name(self):
        city_name = "city name"
        query = MockQuery(city_name=city_name)
        self.assertEqual(self.parameters_builder.build(query=query), {"city": city_name})

    def test_defined_zip_code(self):
        zip_code = "zip code"
        query = MockQuery(zip_code=zip_code)
        self.assertEqual(self.parameters_builder.build(query=query), {"zip": zip_code})

    def test_defined_country_code(self):
        country_code = "country code"
        query = MockQuery(country_code=country_code)
        self.assertEqual(self.parameters_builder.build(query=query), {"country": country_code.upper()})

    def test_defined_page(self):
        page = "page"
        query = MockQuery(page=page)
        self.assertEqual(self.parameters_builder.build(query=query), {"page": page})

    def test_defined_per_page(self):
        per_page = PerPage.ten
        query = MockQuery(per_page=per_page)
        self.assertEqual(self.parameters_builder.build(query=query), {"per_page": per_page.value})
