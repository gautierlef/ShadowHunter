from team import Team
from location import Location
from character import Character
from player import Player
from cards import Card
from rolls import *


def team_all_dead(team):
    all_dead = True
    for player in team:
        if not player.is_dead():
            all_dead = False
    return all_dead


if __name__ == '__main__':
    emi = Character('Emi', 10, 'Hunters');
    franklin = Character('Franklin', 12, 'Hunters')
    george = Character('George', 14, 'Hunters')
    metamorphe = Character('Métamorphe', 11, 'Shadow')
    vampire = Character('Vampire', 13, 'Shadow')
    werewolf = Character('Loup-Garou', 14, 'Shadow')
    allie = Character('Allie', 8, 'Neutres')
    bob = Character('Bob', 10, 'Neutres')
    charles = Character('Charles', 11, 'Neutres')
    daniel = Character('Daniel', 13, 'Neutres')
    locations = [
        Location('Refuge de l\'hermite', [2, 3]),
        Location('Porte de l\'Outremonde', [4, 5]),
        Location('Monastère', [6]),
        Location('Cimetière', [8]),
        Location('Forêt hantée', [9]),
        Location('Sanctuaire ancien', [10])
    ]
    players = [
        Player(emi, 1),
        Player(franklin, 2),
        Player(metamorphe, 3),
        Player(vampire, 4)
    ]
    hunters = [players[0], players[1]]
    shadow = [players[2], players[3]]
    print(*locations, sep='\n')
    print(*players, sep='\n')
    turn = 0
    test = ''
    while not team_all_dead(hunters) and not team_all_dead(shadow) and test != 'exit':
        print('Tour du joueur ' + str(turn + 1))
        test = input()
        if test == '1' or test == '2' or test == '3' or test == '4':
            if not players[int(test)].is_dead():
                players[turn].attack(players[int(test) - 1])
            else:
                print("Joueur déjà mort")
                turn -= 1
        turn += 1
        if turn > 3:
            turn = 0
        print(*players, sep='\n')
    if team_all_dead(hunters):
        print('Shadow win!')
    if team_all_dead(shadow):
        print('Hunters win!')