
list1 = [6, 19, 23, 49, 8, 41, 20, 53, 56, 87]

def find_max(itemlist):
    if len(itemlist) == 1:
        return itemlist[0]
    
    op1 = itemlist[0]
    op2 = find_max(itemlist[1:])

    if op1 > op2:
        return op1
    else:
        return op2


print(find_max(list1))
