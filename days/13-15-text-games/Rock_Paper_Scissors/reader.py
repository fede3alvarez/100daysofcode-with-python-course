import csv 

def read_rolls(roll: str = None):
    '''
    Function retrives file 'battle-table.csv' with rolls data
    Based on the argument (roll string) it return:
        List 1: All rolls that the current roll can defeat
        List 2: All rolls that the current roll will be defeated by
    If no arguments are specified, it prints all data to the console
    '''
    win = []
    lose = []
    draw = []
    with open('battle-table.csv') as fin:
        reader = csv.DictReader(fin)

        # Iterate over each row / roll in the data
        for row in reader:
            if roll is None:
                read_roll(row)
            else:
                name = row['Attacker']
                # If current row / roll matches target roll
                if roll == name:
                    for other_rolls in row:
                        if row[other_rolls] == "win":
                            win.append(other_rolls)
                        elif row[other_rolls] == "lose":
                            lose.append(other_rolls)
                        else:
                            draw.append(other_rolls)
                    return win, lose, draw


def read_roll(row: dict):
    name = row['Attacker']
    del row['Attacker']
    del row[name]

    print("Roll: {}".format(name))
    for k in row.keys():
        can_defeat = row[k].strip().lower() == 'win'
        print(" * {} will defeat {}? {}".format(name, k, can_defeat))
