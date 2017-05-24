from enum import Enum


class PriceRange(Enum):
    one_dollar = 1
    two_dollars = 2
    three_dollars = 3
    four_dollars = 4


class PerPage(Enum):
    five = 5,
    ten = 10,
    fifteen = 15,
    twenty_five = 25,
    fifty = 50,
    one_hundred = 100
