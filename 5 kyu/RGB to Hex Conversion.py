# https://www.codewars.com/kata/513e08acc600c94f01000001/


def rgb(r, g, b):
    
    rgb = [r, g, b]
    
    for index, element in enumerate(rgb):
        if element < 0:
            rgb[index] = 0
            
        elif element > 255:
            rgb[index] = 255
            
    rgb = tuple(rgb)
            
    return ('%02x%02x%02x' % rgb).upper()
