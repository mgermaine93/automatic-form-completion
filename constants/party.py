# thanks to https://project.wnyc.org/party-name-generator/
# this can be used to generate the group name
# https://stackoverflow.com/questions/9828876/find-javascript-function-definition-in-chrome

from random import choice

# constants to be used in the get_group() method of the Floridian class
WORDS = {
    "political_stance": [
        "Formerly Liberal'",
        "Conservative",
        "Independent",
        "Federalist",
        "Anarchist",
        "Libertarian",
        "Moderate",
        "The Callipygians'",
        "Republican"
    ],
    "single_phrase": [
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
        "the Dead",
        "the Callipygians",
        "the Liberals"
    ],
    "political_people": [
        "Former Liberals",
        "Conservative",
        "Independent",
        "Federalist",
        "Anarchist",
        "Libertarian",
        "Democratic",
        "Moderate",
        "Revolutionary",
        "Bolshevik",
        "Single Moms",
        "Children",
        "Seniors",
        "Grandmas",
        "Grandpas",
        "Nudist",
        "Callipygian",
        "Republicans"
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
        "Old-Fashioned",
        "Young",
        "Geriatric"
    ],
    "put_nouns": [
        "Our Children",
        "Wildlife",
        "the Environment",
        "Freedom",
        "Sanity",
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
        "Labor",
        "Out Buttocks"
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
    ],
    "affiliation": [

    ]
}


def pickWord(kind_of_word):
    """
    picks one of the words from the array of kinds(ie "adjective") available
    return the word in that random position in the array
    """
    random_number = choice(range(0, len(WORDS[kind_of_word])))
    word = WORDS[kind_of_word][random_number]
    return word


def make_group_name(version=choice(range(0, 6))):
    """
    passing the version number picks which construction to use
    """
    group_name = ""

    if version == 0:
        group_name = f'{pickWord("political_stance")} {pickWord("political_stance_noun")} Party'
    elif version == 1:
        group_name = f'Put {pickWord("put_nouns")} {pickWord("order")} Party'
    elif version == 2:
        group_name = f'{pickWord("single_phrase")} Party'
    elif version == 3:
        group_name = f'{pickWord("beginning")} {pickWord("general_nouns")} Party'
    elif version == 4:
        group_name = f'{pickWord("adjectives")} {pickWord("political_people")} Party'
    elif version == 5:
        group_name = f'Tax {pickWord("tax_person")} Party'

    return group_name
