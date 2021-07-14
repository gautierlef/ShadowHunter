class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.current_hp = 0

    def __str__(self):
        return 'Name : ' + self.name + ' - HP : ' + str(self.hp)
