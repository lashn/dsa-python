A='ABCGAGAG'
GC =0
GAC =0
for i in reversed(A):

    if i=='G':
        GC =GC +1
    if i=='A':
        GAC =GAC +GC

print(GAC)


# #find a to G
# #to optimize we dont need to run whole array n times of A and G
# #instead will use a counter and Anos

# #2 counters 1 for A and 1 for G
# AGnos=0
# #counts - both A -> Ano of G's
# Acount=0
# for i in range(len(A)):
#     if A[i]=='A':
#         Acount+=1
#     if A[i]=='G':
#         AGnos=Acount*AGnos+1
# return AGnos
