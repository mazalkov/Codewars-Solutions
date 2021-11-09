# https://www.codewars.com/kata/554e4a2f232cdd87d9000038
# after looking at best practices, I learned that you can
# use string translation in Python to make this much cleaner

def DNA_strand(dna):
    # code here
    dna = list(dna)
    
    for position, value in enumerate(dna):
        
        if value == 'A':
            dna[position] = 'T'
            
        if value == 'T':
            dna[position] = 'A'
            
        if value == 'C':
            dna[position] = 'G'
            
        if value == 'G':
            dna[position] = 'C'
            
    dna = ''.join(dna)
    
    return dna
