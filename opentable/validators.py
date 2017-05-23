import us
import pycountry

from query_parameters import PriceRange, PerPage


class RestaurantQueryValidator:
    def __init__(self):
        pass

    def is_valid(self, query):
        isinstance(query.price, PriceRange)
        isinstance(query.per_page, (None, PerPage),)

    def valid_types(self, query):
        isinstance(query.price, (None, PriceRange),)
        isinstance(query.per_page, (None, PerPage),)
        isinstance(query.address_line, basestring)
        isinstance(query.state_code, basestring)
        isinstance(query.city, basestring)
        isinstance(query.zip_code, basestring)
        isinstance(query.country_code, basestring)
        isinstance(query.page, int)

    def is_valid_state_code(self, state_code):
        return us.states.lookup(val=state_code.upper(), field="abbr") is not None

    def is_valid_country_code(self, country_code):
        try:
            return pycountry.countries.get(alpha_2=country_code.upper()) is not None
        except BaseException:
            return False

    def one_present_query_parameter(self, query):
        return query.price is not None \
            or query.name is not None \
            or query.address_line is not None \
            or query.state_code is not None \
            or query.city is not None \
            or query.zip_code is not None \
            or query.country_code is not None
