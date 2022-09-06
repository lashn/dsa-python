# a=3
# n=4
# p=7
# p=100009
# #a**n%p
# ans=1
# for i in range(n):
#     ans*=a
# mod=ans%p
# print(f"before mod {ans}")
# print(f"after mod {mod}")


# a=2
# n=40
# p=10**40+7
# #a**n%p
# ans=1
# for i in range(n):
#     ans*=a
# mod=ans%p
# print(f"before mod {ans}")
# print(f"after mod {mod}")

# above wil fail in other prog langs, overflow doesnt occur in python as no int or float or long

a=2
n=40
p=10**40+7
#a**n%p
ans=1
for i in range(n):
    ans=ans%p*a%p
mod=ans
print(f"before mod {ans}")
print(f"after mod {mod}")

