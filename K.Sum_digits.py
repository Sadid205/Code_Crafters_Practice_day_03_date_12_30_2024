def sum_array(array):
    sum = 0
    for value in array:
        sum = sum+value
    print(sum)

size = int(input(""))
S = input("")
new_array = [int(num) for num in S]
sum_array(new_array)
