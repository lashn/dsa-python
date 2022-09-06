# def factorial(num):
#     prod = 1
#     for i in range(1, num + 1):
#         prod *= i
#     return prod
#
#
# # don't touch above this line
#
#
# def test(num):
#     fact = factorial(num)
#     print(f"The factorial of {num} is {fact}")
#
#
# test(0)
# test(4)
# test(5)
# test(7)
# test(9)
# test(13)
# test(15)
# test(14)


#recursion factorial

def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)

# fact(n=2) -> 2*fact(n=1)
#     fact(n=1) -> 1*fact(0)
#         fact(n=0) -> 1

num=5
print(fact(num))