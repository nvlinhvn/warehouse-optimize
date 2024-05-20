from functions import load_data, write_solution, total_distance


# Load the problem data
items, item_widths, orders = load_data("data.json")

### LINH VIET NGUYEN SOLUTION BELOW #######################################

best_item_sequence = ['Malm', 'Dvala', 'Ribba', 'Lack', 'Ektorp',
                      'Billy', 'Fargrik', 'Klippan', 'Stockholm', 'Poang',
                      'Frakta', 'Docksta', 'Kallax', 'Raskog']
best_door_offset = 10.9
best_orders = [  
                 ['Billy'],
                 ['Dvala', 'Malm', 'Stockholm', 'Poang'],
                 ['Dvala', 'Ribba', 'Billy', 'Fargrik', 'Poang', 'Docksta'],
                 ['Ektorp'],
                 ['Billy', 'Poang'],
                 ['Ektorp', 'Fargrik', 'Frakta', 'Docksta'],
                 ['Fargrik', 'Poang', 'Frakta', 'Raskog', 'Malm'],
                 ['Poang', 'Ektorp'],
                 ['Klippan'],
                 ['Dvala', 'Klippan', 'Poang', 'Frakta', 'Docksta', 'Kallax'],
                 ['Dvala', 'Lack', 'Ektorp', 'Billy', 'Kallax'],
                 ['Raskog', 'Dvala', 'Ribba'],
                 ['Dvala', 'Ribba', 'Lack', 'Stockholm', 'Poang', 'Kallax'],
                 ['Frakta', 'Ribba', 'Lack'],
                 ['Dvala'],
                 ['Docksta', 'Stockholm', 'Klippan'],
                 ['Ribba', 'Malm', 'Stockholm', 'Raskog'],
                 ['Lack', 'Malm', 'Ektorp', 'Stockholm', 'Docksta'],
                 ['Stockholm', 'Frakta', 'Ribba'],
                 ['Malm', 'Billy', 'Stockholm', 'Klippan'],
                 ['Docksta', 'Stockholm', 'Ribba'],
                 ['Ektorp', 'Dvala', 'Malm', 'Klippan', 'Stockholm', 'Poang'],
                 ['Dvala', 'Ektorp', 'Billy', 'Fargrik', 'Stockholm'],
                 ['Raskog', 'Docksta', 'Billy', 'Lack', 'Malm'],
                 ['Lack'],
                 ['Dvala', 'Frakta', 'Docksta', 'Raskog'],
                 ['Ribba', 'Ektorp', 'Billy', 'Klippan', 'Frakta', 'Kallax'],
                 ['Stockholm', 'Poang', 'Raskog', 'Fargrik', 'Billy', 'Dvala'],
                 ['Ribba'],
                 ['Ektorp', 'Lack', 'Billy', 'Fargrik', 'Klippan'],
                 ['Dvala'],
                 ['Dvala', 'Ribba'],
                 ['Klippan', 'Stockholm', 'Kallax', 'Raskog', 'Billy'],
                 ['Billy', 'Fargrik', 'Ektorp'],
                 ['Malm', 'Lack', 'Ektorp', 'Billy'],
                 ['Dvala', 'Billy', 'Frakta'],
                 ['Stockholm'],
                 ['Dvala', 'Lack', 'Ektorp', 'Stockholm', 'Docksta'],
                 ['Malm', 'Billy', 'Fargrik', 'Docksta', 'Kallax'],
                 ['Lack', 'Ektorp'],
                 ['Fargrik', 'Billy'],
                 ['Poang', 'Kallax', 'Raskog', 'Dvala'],
                 ['Billy', 'Ribba', 'Fargrik'],
                 ['Ektorp'],
                 ['Poang'],
                 ['Ektorp', 'Ribba', 'Klippan', 'Poang', 'Docksta'],
                 ['Billy', 'Fargrik', 'Frakta', 'Docksta', 'Kallax', 'Raskog'],
                 ['Ribba'],
                 ['Lack', 'Ektorp', 'Billy', 'Klippan', 'Poang'],
                 ['Billy', 'Ribba', 'Dvala', 'Kallax'],
                 ['Malm', 'Stockholm', 'Poang', 'Frakta', 'Kallax']
              ]

### LINH VIET NGUYEN SOLUTION ABOVE #######################################

# Write the solution
write_solution(best_item_sequence, best_door_offset, best_orders)

# Print results
score = total_distance(best_item_sequence,
                       best_door_offset,
                       item_widths,
                       best_orders)
print("Score = {}".format(round(score, 2)))
