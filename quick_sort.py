def quick_sort(array, first, last):
    if first < last:
        pivotIdx = partition(array, first, last)

        quick_sort(array, first, pivotIdx-1)
        quick_sort(array, pivotIdx+1, last)

def partition(values, first, last):
    pivotvalue = values[first]
    
    lower = first + 1
    upper = last

    done = False

    while not done:
        while lower <= upper and values[lower] <= pivotvalue:
            lower += 1

        while values[upper] >= pivotvalue and upper >= lower:
            upper -= 1
        
        if upper < lower:
            done = True
        else:
            values[lower], values[upper] = values[upper], values[lower]

    values[first], values[upper] = values[upper], values[first]
    
    return upper

items = [1,2,3,89, 5, 60, 31, 48, 100, 53]
quick_sort(items, 0, len(items)-1)
print(items)