# def nat(n):
#     sum=0
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             sum=sum+1
#     return sum
# n=5
# print(nat(n))


def nat(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
n=5
print(nat(n))