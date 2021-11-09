# used to make changes to large city/town lists more efficient
towns = [
    "Tampa", "St. Petersburg", "Clearwater", "Lakeland", "Riverview", "Brandon", "Spring Hill", "Apollo Beach", "Bayonet Point", "Bloomingdale", "Citrus Park", "Cheval", "Dunedin", "Egypt Lake-Leto", "East Lake", "East Lake-Orient Park", "Elfers", "Fish Hawk", "Greater Carrollwood", "Greater Northdale", "Gulfport", "Holiday", "Hudson", "Jasmine Estates", "Keystone", "Lake Magdalene", "Land o' Lakes", "Largo", "Lealman", "Lutz", "New Port Richey", "Mango", "Oldsmar", "Palm Harbor", "Palm River-Clair Mel", "Pinellas Park", "Plant City", "Ruskin", "Safety Harbor", "Shady Hills", "Seminole", "Sun Center", "Tarpon Springs", "Temple Terrace", "Thonotosassa", "Town 'n' Country", "Trinity", "Valrico", "Wesley Chapel", "West Lealman", "Westchase", "Zephyrhills"
]

new_towns = []
for town in towns:
    new_towns.append(town + ", FL")
print(new_towns)
