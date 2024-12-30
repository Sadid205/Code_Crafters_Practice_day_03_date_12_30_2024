





q = int(input(""))
while q>0:
    S = input("")
    if len(S)>10:
        first_charecter = S[0]
        last_charecter = S[len(S)-1]
        count = 0
        for i in range(1,len(S)-1):
            count = count+1
        print(first_charecter+str(count)+last_charecter)
    else:
        print(S)
    q = q-1