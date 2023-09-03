def Fibo(n):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return Fibo(n-1) + Fibo(n-2)
    

k = int(input())
print(Fibo(k))