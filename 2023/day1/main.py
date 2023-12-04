# create numbers with first and last digit.  if only 1 digit, double it to make the nuber
# sum

from collections import defaultdict

# import input file as list

with open('input.txt') as fp:
    lst = fp.read().split('\n')

import re

def convert_to_numbers(s):
    words_to_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for key,value in words_to_numbers.items():
        s = s.replace(key, value)

    return s

def convert_re(s):
    new_s = re.findall('(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))', s)
    new_s = ''.join(new_s)

    words_to_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for key,value in words_to_numbers.items():
        new_s = new_s.replace(key, value)

    print(new_s)
    return new_s

sum = 0
for str in lst:
    print(str)
    new_str = convert_re(str)
    print(new_str)
    digits = [int(i) for i in new_str if i.isdigit()]
    if len(digits) == 1:
        sum += digits[0] * 10 + digits[0]
    else:
        num1 = digits[0]
        num2 = digits[-1]
        print(num1, num2)
        sum += num1 * 10 + num2
        print(sum)


print(sum)