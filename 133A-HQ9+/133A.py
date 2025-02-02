
def isCode(ls): 
    acpr = ['H', 'Q', '9']
    
    for code in ls: 
        if code in acpr: 
            return ('YES')
    
    return('NO')


a = str(input())
ls = list(a)
print(isCode(ls))