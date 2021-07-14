from datetime import datetime
import random

random.seed(datetime.now())


def roll_attack():
    d4 = random.randint(1, 4)
    d6 = random.randint(1, 6)
    print(d4, d6)
    return abs(d6 - d4)


def roll_location():
    d4 = random.randint(1, 4)
    d6 = random.randint(1, 6)
    print(d4, d6)
    return d4 + d6


def roll_teams_4_players():
    p1 = 1
    p2 = 2
    p3 = 2
    p4 = 1


def roll_shadow_hunter():
    random.randint(0, 2)
