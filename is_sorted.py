
list1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
list2 = [6, 19, 23, 49, 8, 41, 20, 53, 56, 87]

def is_sorted(itemlist):
    for i in range(len(itemlist) - 1):
        if itemlist[i] > itemlist[i+1]:
            return False
    return True

    # return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist) - 1))

print(is_sorted(list1))
print(is_sorted(list2))
