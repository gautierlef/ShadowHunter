class Player:
    def __init__(self, number, character):
        self.number = number
        self.current_hp = 0
        self.character = character

    def __str__(self):
        return 'Player : ' + self.number + ' - Current HP : ' + str(self.current_hp)
