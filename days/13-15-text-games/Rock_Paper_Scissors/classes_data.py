import reader

class Roll:
    def __init__(self, roll_name):
        self.roll_name = name
        self.win, self.lose, self.draw = reader.read_rolls(roll_name)

    def match(self, adversary):
        result = None
        if adversary in self.win:
            result = "win"
        elif adversary in self.lose:
            result = "lose"
        elif adversary in self.draw:
            result = "draw"
        else:
            result = "error"
        return results

class Player:
    def __init__(self, name):
        self.name = name
