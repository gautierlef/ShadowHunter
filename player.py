from rolls import *


class Player:
    def __init__(self, character, order):
        self.character = character
        self.order = order
        self.current_damage = 0
        self.current_location = None
        self.equipment = []
        self.revealed = False

    def __str__(self):
        return 'Player ' + str(self.order) + ' - Current HP : ' + str(self.current_damage)

    def attack(self, attacked_player):
        attacked_player.current_damage += roll_attack()
        print('Joueur ' + str(self.order) + ' attaque le joueur ' + str(attacked_player.order))

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
                self.reveal_character()
            return True
        return False
