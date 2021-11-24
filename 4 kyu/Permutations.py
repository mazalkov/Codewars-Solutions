# https://www.codewars.com/kata/5254ca2719453dcc0b00027d


import itertools


def permutations(string):
    
    # admittedly confusing since the function is also permutations
    perms = [''.join(p) for p in itertools.permutations(string)]
    
    return set(perms)
