class Team(list):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Team : ' + self.name
