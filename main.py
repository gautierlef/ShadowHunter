from team import Team
from location import Location
from character import Character
from rolls import *

if __name__ == '__main__':
    hunters = Team('Hunters')
    shadow = Team('Shadow')
    neutrals = Team('Neutres')
    hunters.append(Character('Emi', 10))
    hunters.append(Character('Franklin', 12))
    hunters.append(Character('George', 14))
    shadow.append(Character('Métamorphe', 11))
    shadow.append(Character('Vampire', 13))
    shadow.append(Character('Loup-Garou', 14))
    neutrals.append(Character('Allie', 8))
    neutrals.append(Character('Bob', 10))
    neutrals.append(Character('Charles', 11))
    neutrals.append(Character('Daniel', 13))
    locations = [
        Location('Refuge de l\'hermite', [2, 3]),
        Location('Porte de l\'Outremonde', [4, 5]),
        Location('Monastère', [6]),
        Location('Cimetière', [8]),
        Location('Forêt hantée', [9]),
        Location('Sanctuaire ancien', [10])
    ]
    print(hunters, *hunters, sep='\n')
    print(shadow, *shadow, sep='\n')
    print(neutrals, *neutrals, sep='\n')
    print(*locations, sep='\n')
    print(roll_location())
    print(roll_attack())

