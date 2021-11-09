# used to make changes to large city/town lists more efficient
towns = [
    'Bloomington', 'Brooklyn Center', 'Brooklyn Park', 'Champlin', 'Chanhassen', 'Corcoran', 'Crystal', 'Dayton', 'Deephaven', 'Eden Prairie', 'Edina', 'Excelsior', 'Golden Valley', 'Greenfield', 'Greenwood', 'Hanover', 'Hopkins', 'Independence', 'Long Lake', 'Loretto', 'Maple Grove', 'Maple Plain', 'Medicine Lake', 'Medina', 'Minneapolis', 'Minnetonka', 'Minnetonka Beach', 'Minnetrista', 'Mound', 'New Hope', 'Orono', 'Osseo', 'Plymouth', 'Richfield', 'Robbinsdale', 'Rockford', 'Rogers', 'Shorewood', 'Spring Park', 'St. Anthony', 'St. Bonifacius', 'St. Louis Park', 'Tonka Bay', 'Wayzata', 'Woodland'
]

new_towns = []
for town in towns:
    new_towns.append(town + ", MN")
print(new_towns)
