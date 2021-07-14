class Character:
    def __init__(self, name, hp, team):
        self.hp = hp
        self.team = team
        self.name = name
        self.description = ''

    def __str__(self):
        return 'Name : ' + self.name + ' - HP : ' + str(self.hp)
