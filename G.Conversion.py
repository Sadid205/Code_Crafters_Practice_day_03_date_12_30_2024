def Conversion(S):
    newString = []
    for C in S:
        Asci = ord(C)
        if Asci>=97 and Asci<=122:
           uppercase =  Asci-32
           newString.append(chr(uppercase))
        elif Asci >=65 and Asci<=90:
            lowercase = Asci+32
            newString.append(chr(lowercase))
        else:
            newString.append(" ")
    for c in newString:
        print(c,end="")
        
S=input("")
Conversion(S)