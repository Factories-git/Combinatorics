def factorial(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s


n, k = map(int, input().split())
print((factorial(n) // factorial(n-k)) // factorial(k))