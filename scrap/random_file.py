# used to make changes to large city/town lists more efficient
towns = [
    'Alamo', 'Alton', 'Donna', 'Edcouch', 'Edinburg', 'Elsa', 'Granjeno', 'Hidalgo', 'La Joya', 'La Villa', 'McAllen', 'Mercedes', 'Mission', 'Palmhurst', 'Palmview', 'Penitas', 'Pharr', 'Progreso', 'Progreso Lakes', 'San Juan', 'Sullivan City', 'Weslaco', 'edit', 'Abram', 'Alton North', 'César Chávez', 'Citrus City', 'Cuevitas', 'Doffing', 'Doolittle', 'Faysville', 'Harding Gill Tract', 'Hargill', 'Havana', 'Heidelberg', 'Indian Hills', 'La Blanca', 'La Coma Heights', 'La Homa', 'Laguna Seca', 'Linn', 'Llano Grande', 'Lopezville', 'Los Ebanos', 'Midway North', 'Midway South', 'Mila Doce', 'Monte Alto', 'Muniz', 'Murillo', 'North Alamo', 'Olivarez', 'Palmview South', 'Perezville', 'Relampago', 'Salida del Sol Estates', 'San Carlos', 'Scissors', 'South Alamo', 'Villa Verde', 'West Sharyland', 'edit', 'McCook'
]

new_towns = []
for town in towns:
    new_towns.append(town + ", TX")
print(new_towns)
