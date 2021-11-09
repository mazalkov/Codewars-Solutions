# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa

def open_or_senior(data):
    
    out = []
    
    for element in data:
        if element[0] >= 55 and element[1] > 7:
            out.append("Senior")
            
        else:
            out.append("Open")
        
    return out
