# 1-savol
def zero_count(n,m):
    sum = 1
    for i in range(n,m):
        sum *= i
    sum = str(sum)
    return sum.count('0')

n = int(input("n= "))
m = int(input("m= "))

print(zero_count(n,m))
