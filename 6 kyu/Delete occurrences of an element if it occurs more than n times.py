# https://www.codewars.com/kata/554ca54ffa7d91b236000023


def delete_nth(order,max_e):
    
    ans = []

    for element in order:
        
        if ans.count(element) < max_e:
            ans.append(element)
            
            
    return ans
