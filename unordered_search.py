items = [20, 8, 6, 18, 10, 4, 29, 19]

def find_item(item, itemlist):
    for i in range(len(items)):
        if item == itemlist[i]:
            return i
    
    return None

print(find_item(29, items))
print(find_item(5, items))