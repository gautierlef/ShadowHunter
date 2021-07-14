class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return 'Name : ' + self.name + ' - HP : ' + str(self.hp)
