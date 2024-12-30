def Frequency(N,M,A):
    count = [0]*(M+1)
    for i in range(0,N):
        count[A[i]] = count[A[i]]+1
    for i in range(1,M+1):
        print(count[i])


N_M = input("")
A = input("")
split_N_M = N_M.split()
N = int(split_N_M[0])
M = int(split_N_M[1])
split_A = A.split()
A = [int(num) for num in split_A]
Frequency(N,M,A)


