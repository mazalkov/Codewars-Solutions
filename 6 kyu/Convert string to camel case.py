# https://www.codewars.com/kata/517abf86da9663f1d2000003


import re


def to_camel_case(text):
    
    split_text = re.split(r'\s|[-_]', text)
    
    for i in range(1, len(split_text)):
        split_text[i] = split_text[i].title()
        
    return ''.join(split_text)
