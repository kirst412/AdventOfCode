# imports
from collections import defaultdict


# import data
with open('input.txt') as fp:
    lst = fp.read().split('\n')


#read in as one list with a long string in it
# create algo that determines if last 4 chars are different

for i,char in enumerate(lst[0]):
    if i >= 13:
        # grab last 4 chars and see if any of them match, do a set/list type thing and check length
        last4 = lst[0][i-13:i+1]
        last4_lst = [a for a in last4]
        len_last4_lst = len(last4_lst)
        len_last4_set = len(list(set(last4_lst)))
        if len_last4_set == len_last4_lst:
            print(i+1)
            break


