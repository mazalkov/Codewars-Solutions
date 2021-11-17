# https://www.codewars.com/kata/550498447451fbbd7600041c


def comp(array1, array2):
    
    
    if array1 is None or array2 is None:
        return False
           
    if not array1 and not array2:
        return True
    
    if not array1 or not array2:
        return False

    
    array1 = sorted([i**2 for i in array1])
    array2 = sorted(array2)
        
    return array1 == array2
