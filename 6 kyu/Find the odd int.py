# https://www.codewars.com/kata/54da5a58ea159efa38000836/


def find_it(seq):
    
    for element in seq:
        if (seq.count(element) % 2) != 0:
            return element
