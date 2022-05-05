# Fetch csv file
# to do

# Confirms valid roll based on csv data
def confirm_roll():
    pass

class Roll(roll=None):
    def __init__(self, roll):
        if confirm_roll(roll):
            self.roll = roll
        else:
            self.roll = None

class Player(name):
    def __init__(self, name):
        self.name = name
