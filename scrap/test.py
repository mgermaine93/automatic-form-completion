from __future__ import print_function  # Py 2.6+; In Py 3k not needed

import csv

def get_cities_and_area_codes_in_state():
    with open('us-area-code-cities.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            print(row)
            new_row = ""
            if row[1][0] == '"' and row[1][-1] == '"' and row[2][0] == '"' and row[2][-1] == '"':
                new_row == f'{row[0]},{row[1][1:-1]},{row[2][1:-1]},{row[3]},{row[4]},{row[5]},'
            elif row[1][0] == '"' and row[1][-1] == '"':
                new_row == f'{row[0]},{row[1][1:-1]},{row[2]},{row[3]},{row[4]},{row[5]},'
            elif row[2][0] == '"' and row[2][-1] == '"':
                new_row == f'{row[0]},{row[1]},{row[2][1:-1]},{row[3]},{row[4]},{row[5]},'
            else:
                new_row == f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},'
            # elif row[1][0] != '"' and row[1][0] != '"':
            #     cities.append(f'{row[0]},"{row[1]}",{row[2]},{row[3]},{row[4]},{row[5]}')
            print(new_row)
            with open('cleaned-us-area-code-cities.csv','a') as fd:
                fd.write(new_row)
            
    # print(cities)
    # return cities

results = get_cities_and_area_codes_in_state()
# print(*results,sep='\n')

# with open('cleaned-us-area-code-cities.csv', 'w') as out_file:
#     print(results, file=out_file)  # Python 3.x

