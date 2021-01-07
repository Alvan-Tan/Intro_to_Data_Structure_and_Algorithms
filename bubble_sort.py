def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] =  array[j+1], array[j]

list1 = [10, 8, 90, 34, 5, 2, 57, 80]
bubble_sort(list1)
print(list1)