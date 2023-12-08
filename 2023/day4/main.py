
from collections import defaultdict

with open('input.txt') as fp:
    data = fp.read().split('\n')

# print(data)

card_sum = 0

card_ids = defaultdict()

for card in data:
    numbers = card.split(":")[1]
    # print(card.split(":")[0].split(' '))
    id = [int(item) for item in card.split(":")[0].split(' ') if item.isdigit()][0]
    winners = numbers.split("|")[0].split(" ")
    my_numbers = numbers.split("|")[1].split(" ")
    winners = [int(a) for a in winners if len(a) > 0]
    my_numbers = [int(a) for a in my_numbers if len(a) > 0]
    matches = 0
    card_value = 0.5
    for number in my_numbers:
        if number in winners:
            card_value = card_value * 2
            matches += 1
    if card_value > 0.5:
        card_sum += card_value
    card_ids[id] = (winners, my_numbers, matches)


# print(card_sum)
# print(card_ids)

number_of_cards = 0
match_counter = []
card_order = list(card_ids.keys())

card_sum = 0
cards = defaultdict(int)
multiplier_counter = 0

for key, value in card_ids.items():
    cards[int(key)] += 1
    print(value[2])
    for i in range(1, cards[int(key)] * value[2]+1):
        cards[int(key)+i] += 1
    print(cards)

print(sum([v for k,v in cards.items()]))

# print(card_order)
# i = 0
# while i < len(card_order) and card_order[i] <= list(card_ids.keys())[-1]:
#     id = card_order[i]
#     matches = 0
#     for number in card_ids[id][1]:
#         if number in card_ids[id][0]:
#             matches += 1
#     if matches > 0:
#         for j in range(1, matches+1):
#             idx = card_order.index(id + j)
#             # print(idx)
#             # print(j)
#             card_order.insert(idx, id + j)
#
#     print(id)
#
#     i += 1
#
# print(len(card_order))
# for i,card in enumerate(data):
#     numbers = card.split(":")[1]
#     winners = numbers.split("|")[0].split(" ")
#     my_numbers = numbers.split("|")[1].split(" ")
#     winners = [int(a) for a in winners if len(a) > 0]
#     my_numbers = [int(a) for a in my_numbers if len(a) > 0]
#     number_of_matches = 0
#     for number in my_numbers:
#         if number in winners:
#             number_of_matches += 1


lines = open('input.txt', 'r').readlines()

def part1():
    total = 0
    for line in lines:
        x, y = map(str.split, line.split('|'))
        matches = set(x) & set(y)
        total += 2 ** (len(matches) - 1) if matches else 0
    return total

def part2():
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        x, y = map(str.split, line.split('|'))
        n = len(set(x) & set(y))
        for j in range(i + 1, min(i + 1 + n, len(lines))):
            cards[j] += cards[i]
    return sum(cards)

print(part1(), part2())