items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(target, itemlist):
    lower = 0
    upper = len(itemlist) - 1

    while lower <= upper:
        midpoint = (lower + upper)//2

        if itemlist[midpoint] == target:
            return midpoint
        
        if target > itemlist[midpoint]:
            lower = midpoint + 1
        else:
            upper = midpoint - 1
    
    return None

print(binarysearch(56, items))
print(binarysearch(250, items))
