def isUnique(n): 
    ls = list(map(int, str(n)))
    b = len(ls) == len(set(ls))
    return b



def yearFinder(n): 
    curr_year = n + 1
    while not isUnique(curr_year): 
        curr_year += 1

    return curr_year


print(yearFinder(int(input())))