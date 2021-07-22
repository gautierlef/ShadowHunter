from player import Player
from cards import Card
import settings


def team_all_dead(team):
    all_dead = True
    for player in team:
        if not player.is_dead():
            all_dead = False
    return all_dead


if __name__ == '__main__':
    players = [
        Player(settings.emi, 1),
        Player(settings.franklin, 2),
        Player(settings.metamorphe, 3),
        Player(settings.vampire, 4)
    ]
    hunters = [players[0], players[1]]
    shadow = [players[2], players[3]]
    turn = 0
    player_input = ''
    while not team_all_dead(hunters) and not team_all_dead(shadow) and player_input != 'exit':
        print('\n', *players, sep='\n')
        print('Tour du joueur ' + str(turn + 1))
        current_player = players[turn]
        current_player.set_location()
        near_players = []
        for player in players:
            if current_player.is_near(player):
                near_players.append(player)
        print('Vous vous trouvez dans ' + current_player.current_location.get_name())
        if len(near_players) == 0:
            print('Aucun joueur proche.')
        else:
            print('Les joueurs proches sont :', *near_players, sep='\n')
            player_input = input()
            if player_input == '1' or player_input == '2' or player_input == '3' or player_input == '4':
                if not players[int(player_input)].is_dead():
                    current_player.attack(players[int(player_input) - 1])
                else:
                    print('Joueur déjà mort')
                    turn -= 1
        turn += 1
        if turn > 3:
            turn = 0
    if team_all_dead(hunters):
        print('Shadow win!')
    if team_all_dead(shadow):
        print('Hunters win!')
