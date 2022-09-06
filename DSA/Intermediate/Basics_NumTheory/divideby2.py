# given +ve N, how many times we need to divive by 2 untill it reaches 1


N=[1,2,4,8]
count=0
for i in range(len(N)):
    while N[i]>1:
        N[i]=N[i]/2
        count+=1

print(count)
