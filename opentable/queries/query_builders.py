class RestaurantSearchQueryParametersBuilder:
    def __init__(self):
        pass

    def build(self, query):
        query_parameters = {}
        if query.price_range is not None:
            query_parameters["price"] = query.price_range.value

        if query.name is not None:
            query_parameters["name"] = query.name

        if query.address_line is not None:
            query_parameters["address"] = query.address_line

        if query.state_code is not None:
            query_parameters["state"] = query.state_code.upper()

        if query.city_name is not None:
            query_parameters["city"] = query.city_name

        if query.zip_code is not None:
            query_parameters["zip"] = query.zip_code

        if query.country_code is not None:
            query_parameters["country"] = query.country_code.upper()

        if query.page is not None:
            query_parameters["page"] = query.page

        if query.per_page is not None:
            query_parameters["per_page"] = query.per_page.value

        return query_parameters
