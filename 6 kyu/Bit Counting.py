# https://www.codewars.com/kata/526571aae218b8ee490006f4


def count_bits(n):
  
    n = bin(n)[2:]
    num = 0
    
    for bit in n:
        num += int(bit)
        
    return num
