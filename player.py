from rolls import *
import settings


class Player:
    def __init__(self, character, order):
        self.character = character
        self.order = order
        self.current_damage = 0
        self.current_location = None
        self.equipment = []
        self.revealed = False

    def __str__(self):
        return 'Joueur ' + str(self.order) + ' - Nombre de blessures : ' + str(self.current_damage) + ' - Lieu : ' \
               + str(self.current_location)

    def set_location(self):
        new_location = self.current_location
        while self.current_location == new_location:
            roll = roll_location()
            if roll == 7:
                print('Vous pouvez choisir votre destination.')
                print(*settings.locations, sep='\n')
                player_input = input()
                roll = int(player_input)
                if roll == 2:
                    roll = 3
                if roll == 4:
                    roll = 5
            new_location = next(location for location in settings.locations if location.roll == roll)
        self.current_location = new_location

    def is_near(self, other_player):
        if self == other_player or other_player.current_location is None:
            return False
        if other_player.current_location == self.current_location:
            return True
        if other_player.current_location.roll == 3 and self.current_location.roll == 5 or\
           other_player.current_location.roll == 5 and self.current_location.roll == 3:
            return True
        if other_player.current_location.roll == 6 and self.current_location.roll == 8 or\
           other_player.current_location.roll == 8 and self.current_location.roll == 6:
            return True
        if other_player.current_location.roll == 9 and self.current_location.roll == 10 or\
           other_player.current_location.roll == 10 and self.current_location.roll == 9:
            return True
        return False

    def attack(self, attacked_player):
        if self == attacked_player:
            print('Vous ne pouvez pas vous attaquer vous même.')
            return False
        elif self.is_near(attacked_player):
            damage = roll_attack()
            attacked_player.current_damage += damage
            print('Joueur ' + str(self.order) + ' attaque le joueur ' + str(attacked_player.order) + ' et lui inflige '
                  + str(damage) + ' Blessures.')
            return True
        else:
            print('Le joueur ' + str(attacked_player.order) + ' ne se trouve pas à proximité.')
            return True

    def heal(self, amount):
        self.current_damage -= amount

    def damage(self, amount):
        self.current_damage += amount

    def reveal_character(self):
        self.revealed = True
        print('Le joueur ' + str(self.order) + ' était ' + self.character.name + ' de l\'équipe ' + self.character.team)

    def is_dead(self):
        if self.current_damage >= self.character.hp:
            if not self.revealed:
                self.current_location = None
                self.reveal_character()
            return True
        return False
