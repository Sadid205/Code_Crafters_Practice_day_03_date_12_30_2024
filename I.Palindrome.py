def isPalindrome(S):
    reverse = S[::-1]
    if S==reverse:
        print("YES")
    else:
        print("NO")


S = input("")
isPalindrome(S)