def DString(S1,S2):
    S1Split = list(S1)
    S2Split = list(S2)
    print(len(S1),len(S2))
    print(S1+S2)
    S1First = S1Split[0]
    S2First = S2Split[0]
    S1Split[0] = S2First
    S2Split[0] = S1First
    modified_S1 = "".join(S1Split)
    modified_S2 = "".join(S2Split)
    print(modified_S1,modified_S2)




S1 = input("")
S2 = input("")
DString(S1,S2)



