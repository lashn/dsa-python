a=[10,20,30,4]

b= reversed(a)
print(b) #<list_reverseiterator object at 0x000001E6A6025BA0>

b=list(b)
print(b) # b= list(reversed(a)) right way to reverse
