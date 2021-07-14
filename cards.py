class Card:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return 'Name : ' + self.name + ' - Description : ' + str(self.description)
