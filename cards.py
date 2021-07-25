class Card:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return 'Carte vision :\nNom : ' + self.name + ' - Description :\n' + str(self.description)

    def draw_card(self, roll, player):
        if roll == 0:
            self.vision_mortifere(player)
        elif roll == 1:
            self.vision_divine(player)
        elif roll == 2:
            self.vision_foudroyante(player)
        else:
            self.vision_lugubre(player)


    def vision_mortifere(self, player):
        if player.character.team == 'Hunter':
            player.damage(1)
            print('Joueur ' + str(player.order) + ' subit 1 point de blessure.')
        else:
            print('Rien ne se passe.')

    def vision_divine(self, player):
        if player.character.team == 'Hunter':
            player.heal(1)
            print('Joueur ' + str(player.order) + ' soigne 1 point de blessure.')
        else:
            print('Rien ne se passe.')

    def vision_foudroyante(self, player):
        if player.character.team == 'Shadow':
            player.damage(1)
            print('Joueur ' + str(player.order) + ' subit 1 point de blessure.')
        else:
            print('Rien ne se passe.')

    def vision_lugubre(self, player):
        if player.character.team == 'Shadow':
            player.heal(1)
            print('Joueur ' + str(player.order) + ' soigne 1 point de blessure.')
        else:
            print('Rien ne se passe.')
