def count_letters(S):
    count_array = [0]*26
    for i in range(0,len(S)):
        asci = ord(S[i]) - ord('a')
        count_array[asci] = count_array[asci]+1
    for i in range(0,len(count_array)):
        if count_array[i]!=0:
            print(f"{chr(i+ord('a'))} : {count_array[i]}")

S = input("")
count_letters(S)