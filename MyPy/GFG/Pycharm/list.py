# l=[10,20,50,30,40]
#
# def maxl(l):
#     for x in l:
#         for y in l:
#             if y > x:
#                 break
#         else:
#             return x
#     else:
#         return None
#
# print(maxl(l))

# 2nd large in array
# 2nd large in array
# # l = [60,10,20,30,5,6,40,4,5,50,70]
# l = [60, 60, 50, 10]
#
#
# def slargest(l):
#     fir = l[0]
#     sec = None
#
#     for x in l[1:]:
#         if x > fir:
#             sec = fir
#             fir = x
#         if sec == None or sec < x:
#             sec = x
#
#     return sec
#
#
# print(slargest(l))

# --------------
#check for palindrome
txt="abcba"

print(len(txt))

for i in txt:
    print(i)