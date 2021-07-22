class Location:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return self.name + ' - ' + str(self.roll)

    def get_name(self):
        return self.name
