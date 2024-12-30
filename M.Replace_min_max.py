import sys
def Replace(size,array):
    min = sys.maxsize
    max = -sys.maxsize    

    i = 0
    j = size-1
    while i<j:
        if array[i] > array[j] and array[i]>max:
            max = array[i]
        if array[i] < array[j] and array[i]<min:
            min = array[i]
        if array[j] > array[i] and array[j]>max:
            max = array[j]
        if array[j] < array[i] and array[j]<min:
            min = array[j]
        i = i+1
        j = j-1 
    max_index = array.index(max)
    min_index = array.index(min)
    array[max_index] = min
    array[min_index]  = max
    for i in array:
        print(i,end=" ")


size = int(input(""))
array = input("")
split_input = array.split()
new_array = [int(num) for num in split_input]
Replace(size,new_array)
