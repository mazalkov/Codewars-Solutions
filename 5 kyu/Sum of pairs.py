# https://www.codewars.com/kata/54d81488b981293527000c8f

def sum_pairs(lst, s):
    
    cache = set()
    
    for x in lst:
        
        if s - x in cache:
            return [s - x, x]
        
        cache.add(x)
