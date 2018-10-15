import numpy as np
import os

input = [9, 'a', 'b', 'c', 'c', 'b', 'c', 'b', 'd', 'e']

def get_vote_num(input):
    name_list = input[1:len(input)]
    name_dict = {}

    for name in name_list:
        if name_dict.get(name, False) is False:
            name_dict[name] = 1
        else:
            name_dict[name] = name_dict[name] + 1

    name = max(name_dict, key=name_dict.get)
    vote = max(name_dict.values())

    return name, vote

name, vote = get_vote_num(input)

print('Name of the Candidate:' + name)
print('No. of Votes: %d' % vote)