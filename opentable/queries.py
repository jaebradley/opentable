from query_parameters import PerPage


class RestaurantSearchQuery:
    def __init__(self, price=None, name=None, address_line=None, state_code=None, city=None, zip_code=None,
                 country_code=None, page=1, per_page=PerPage.twenty_five):
        self.price = price
        self.name = name
        self.address_line = address_line,
        self.state_code = state_code,
        self.city = city,
        self.zip_code = zip_code,
        self.country_code = country_code,
        self.page = page
        self.per_page = per_page
