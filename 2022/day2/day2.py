# import data
with open('input.txt') as fp:
    lst = fp.read().split('\n')

# this reads in as a list of 'A X', ... strings

# A = Rock, B = Paper, C = scissors of opponent
# X = Rock, Y = Paper, Z = scissors of myself
# scores: 1, rock; 2, paper; 3, scissors
my_score_guide = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

win_guide = {
    'X': {'A': 3, 'B': 0, 'C': 6},
    'Y': {'A': 6, 'B': 3, 'C': 0},
    'Z': {'A': 0, 'B': 6, 'C': 3}
}



def determine_win(me, them):
    return win_guide[me][them]

def score_round(win, hand):
    return win + my_score_guide[hand]

def part_1():
    # split into your hands and opponents hands
    my_hands = []
    opp_hands = []
    for i in lst:
        my_hands.append(i.split(" ")[1])
        opp_hands.append(i.split(" ")[0])
    # loop through each hand.
    total = 0
    for i,me in enumerate(my_hands):
        them = opp_hands[i]
        win = determine_win(me, them)
        score = score_round(win, me)
        total += score

    print(total)

part_1()

# part 2

# input list is now [opp hand how the round should end]
# X: lose, Y: draw, Z: win

new_score_guide = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

hand_guide = {
    'X': {'A': 3, 'B': 1, 'C': 2},
    'Y': {'A': 1, 'B': 2, 'C': 3},
    'Z': {'A': 2, 'B': 3, 'C': 1}
}

total = 0

def calculate_score(wlt):
    return new_score_guide[wlt]

# split into your hands and opponents hands
wlt = []
opp_hands = []
for i in lst:
    wlt.append(i.split(" ")[1])
    opp_hands.append(i.split(" ")[0])
for i,opp_hand in enumerate(opp_hands):
    total += calculate_score(wlt[i])
    total += hand_guide[wlt[i]][opp_hand]
print(total)

# translate hand guide to free up X,Y,Z again
