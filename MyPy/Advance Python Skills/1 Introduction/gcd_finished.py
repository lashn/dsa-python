# Find the greatest common denominator of two numbers
# using Euclid's algorithm

#
# def gcd(a, b):
#     while (b != 0):
#         t = a       # set aside the value of a
#         a = b       # set a equal to b
#         b = t % b   # divide t (which is a) by b
#
#     return a
#
#
# # try out the function with a few examples
# print(gcd(60, 96))  # should be 12
# print(gcd(20, 8))   # should be 4


#natural numbers
#sum of n = n(n+1)/2



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
        for j in range(1,i+1):
            sum=sum+1
    return sum
n=15
print(nat(n))