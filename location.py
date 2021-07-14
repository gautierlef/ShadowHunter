class Location:
    def __init__(self, name, rolls):
        self.name = name
        self.rolls = rolls

    def __str__(self):
        return 'Location : ' + self.name