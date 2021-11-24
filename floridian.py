# this can be made more object-oriented, particularly with the methods of the Floridian() class.

from random import randint, choice
from constants.areas_and_cities.florida_areas_and_cities import FLORIDA_AREAS_AND_CITIES
from names import get_first_name, get_last_name
from functions import (
    generate_geographic_area,
    generate_city_and_state,
    get_city_from_city_and_state,
    get_state_from_city_and_state,
    generate_last_seven_digits_of_phone_number,
    get_closest_area_code,
)
from person import (
    Person,
    generate_geographic_area,
    generate_city_and_state
)


def generate_florida_county():
    county_and_state = choice(list(FLORIDA_AREAS_AND_CITIES))
    return county_and_state


def generate_florida_city_and_state(geographic_area):
    """
    Needs docstring
    """
    if geographic_area in FLORIDA_AREAS_AND_CITIES.keys():
        city_and_state = {}
        city = choice(FLORIDA_AREAS_AND_CITIES[geographic_area])
        state = geographic_area[-2:]
        city_and_state[city] = state
        return city_and_state
    else:
        raise KeyError(
            f"{geographic_area} wasn't found in the list of available geographic areas.")


class Floridian(Person):

    def __init__(self, first_name=None, last_name=None, city_and_state=None):
        super().__init__(first_name=first_name, last_name=last_name)
        self.city_and_state = city_and_state or generate_florida_city_and_state(
            generate_florida_county())

    def get_geographic_area(self):
        # https://stackoverflow.com/questions/231839/python-inheritance-how-to-disable-a-function
        raise AttributeError(
            "'Floridian' object has no attribute 'get_geographic_area().'")

    def get_city(self):
        return list(self.city_and_state.keys())[0]

    def get_county(self):
        counties = FLORIDA_AREAS_AND_CITIES
        city = list(self.city_and_state.keys())[0]
        for county in counties:
            if city in FLORIDA_AREAS_AND_CITIES[county]:
                return county
        raise KeyError(
            f"{city} was not found in the available dictionary of Florida cities and counties.")

    def get_group(self):
        pass


def get_words():
    words = {
        "political_stance": [
            "Liberal",
            "Conservative",
            "Independent",
            "Communist",
            "Federalist",
            "Socialist",
            "Anarchist",
            "Libertarian",
            "Democratic",
            "Moderate",
            "Centrist",
            "Marxist"
        ],
        "single_phrase": [
            "Like it's 1999",
            "All Tomorrow's",
            "Pity",
            "Thank You Based God",
            "Surprise",
            "LAN",
            "Costume",
            "Slumber",
            "Stop & Frisk",
            "Bring Back Arrested Development",
            "Free Gucci",
            "Tread on Me",
            "Iced Tea",
            "Pizza",
            "After",
            "Paid Vacation"
        ],
        "tax_person": [
            "the Rich",
            "the Poor",
            "Everybody",
            "Grandma",
            "Our Children",
            "the Future",
            "Nobody",
            "America's Job Creators",
            "the Huddled Masses",
            "Freedom",
            "the Dead"
        ],
        "political_people": [
            "Liberal",
            "Conservative",
            "Independent",
            "Communist",
            "Federalist",
            "Socialist",
            "Anarchist",
            "Libertarian",
            "Democratic",
            "Moderate",
            "Centrist",
            "Revolutionary",
            "Marxist",
            "Bolshevik",
            "Single Moms",
            "Orphans",
            "Children",
            "Seniors",
            "Grandmas",
            "Nudist"
        ],
        "political_stance_noun": [
            "Goon",
            "Agitator",
            "Loafer",
            "Thug",
            "Riff-Raff",
            "Freeloader",
            "Crusader",
            "Convict",
            "Martyr",
            "Jerk",
            "Blowhard",
            "Saint",
            "Backlash",
            "Rage",
            "Venom",
            "Revolution",
            "Firestorm"
        ],
        "adjectives": [
            "New",
            "Athletic",
            "Superior",
            "Lazy",
            "Indulgent",
            "Angry",
            "Crazed",
            "Apathetic",
            "Jaded",
            "Salivating",
            "Rambunctious",
            "Bleeding Heart",
            "Manipulative",
            "Caffeinated",
            "Overhyped",
            "Incompetent",
            "Inconsiderate",
            "Evil",
            "Valiant",
            "Stoic",
            "Working",
            "Modern",
            "Old-Fashioned"
        ],
        "put_nouns": [
            "Our Children",
            "Wildlife",
            "the Environment",
            "Freedom", "Sanity",
            "Compassion",
            "Pizza",
            "Transportation",
            "the Economy",
            "Total War",
            "Equal Rights",
            "Seniors",
            "Waste Management",
            "the Proletariat",
            "Currency Manipulation",
            "Tradition",
            "Families",
            "Justice",
            "the Rich",
            "the Poor",
            "World Domination",
            "Labor"
        ],
        "general_nouns": [
            "Wildlife",
            "Alcohol",
            "Marijuana",
            "Fun",
            "Taxes",
            "Prohibition",
            "Pizza",
            "Cash",
            "Gold",
            "Freedom",
            "Poverty",
            "Values",
            "Chaos",
            "Platinum",
            "Equality",
            "Exceptionalism",
            "Jingoism",
            "Lunch Breaks"
        ],
        "beginning": [
            "Modern",
            "Anti-",
            "Pro-",
            "New",
            "Never-Ending",
            "Forever",
            "No",
            "National",
            "American",
            "United",
            "Classic",
            "Traditional",
            "Organized",
            "Grassroots",
            "Patriots for",
            "Americans for",
            "Old-Fashioned"
        ],
        "order": [
            "First",
            "Last",
            "Somewhere in the Middle of Our Priorities",
            "Off Until Tomorrow"
        ]
    }
    return words


# floridian = Floridian()
# print(floridian.first_name)
# print(floridian.last_name)
# print(floridian.city_and_state)
# print(floridian.get_county())
# print(floridian.generate_phone_number())
