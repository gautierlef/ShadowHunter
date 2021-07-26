from player import Player
import settings
from rolls import roll_vision_card


def team_all_dead(team):
    all_dead = True
    for player in team:
        if not player.is_dead():
            all_dead = False
    return all_dead


def correct_input(input):
    if input == '1' or input == '2' or input == '3' or input == '4' or input == 'skip' or input == 'exit':
        return True
    return False


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
        player_input = ''
        attack_success = False
        current_player = players[turn]
        current_player.set_location()
        near_players = []
        for player in players:
            if current_player.is_near(player):
                near_players.append(player)
        print('Vous vous trouvez dans ' + current_player.current_location.get_name())
        if current_player.current_location == settings.locations[0]:
            roll = roll_vision_card()
            card = settings.vision_cards[roll]
            print(card)
            print('A qui voulez vous appliquer l\'effet ?')
            while (player_input != '1' and player_input != '2' and player_input != '3' and player_input != '4'
                   and player_input != 'skip'):
                player_input = input()
                if correct_input(player_input) and player_input != 'skip':
                    if not players[int(player_input) - 1].is_dead():
                        card.draw_card(roll, players[int(player_input) - 1])
                    else:
                        print('Joueur déjà mort')
                        player_input = ''
        player_input = ''
        if len(near_players) == 0:
            print('Aucun joueur proche.')
        else:
            while not attack_success and player_input != 'exit' and player_input != 'skip':
                attack_success = False
                print('Les joueurs proches sont :', *near_players, sep='\n')
                player_input = input()
                if correct_input(player_input) and player_input != 'skip':
                    if not players[int(player_input) - 1].is_dead():
                        attack_success = current_player.attack(players[int(player_input) - 1])
                    else:
                        print('Joueur déjà mort')
        turn += 1
        if turn > 3:
            turn = 0
    if team_all_dead(hunters):
        print('Shadow win!')
    if team_all_dead(shadow):
        print('Hunters win!')
