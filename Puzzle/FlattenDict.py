

# validation
# if not isinstance(type(input2),list):
#     print('invalid')

# def rec(input,n):
#     for x in input:
#         if type(x)==list:
#             rec(x,len(x))
#         else:
#             print(x)

# def rec2(input):
#     for i in input:
#         if type(i) == list:
#             result = rec2(i)
#         else:
#             result.append(i)
#     return result

class solution:
    def __init__(self):
        self.result=[]

    def rec2(self,input):
        for i in input:
            if type(i) == list:
                result = self.rec2(self,i)
            else:
                result.append(i)
        return result


class main(solution):
    # input= [1,2,3,[4]]
    # output = [1,2,3,1,5,4,5]
    input2 = [[1], [2, 3], [1, 5, [4, 5]], [[[[2]]]]]
    input3 = [0, [1], [2, 3], [1, 5, [4, 5]]]
    # rec(input2,len(input))
    input = [[1], [2, 3], [1, 5, [4, 5]]]
    sol=solution()
    print(solution.rec2(solution,input))
