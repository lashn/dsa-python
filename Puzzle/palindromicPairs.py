# find all palindromic pairs ex: reward and drawer
# radar signle word palindrom

words=["reward","drawer","mat","tam","abc", "radar"]

'''
approach
reward
if sorted its going to be same for 2 words
traverse across and make init pairs
then traverse pairs and see if they are a match
if individual word then again find
'''
class PalResult():
    def __init__(self):
        self.pal_list=[]

    def group_palin(self, words):
        pal_dict={}
        for i in words:
            sortword="".join(sorted(i))
            if sortword in pal_dict:
                pal_dict[sortword].append(i)
            else:
                pal_dict[sortword]=[i]

        print(pal_dict)

        for k,pair in pal_dict.items():
            if len(pair)>1:
                self.find_palin_pairs(pair)
            else:
                self.find_palin_one(pair)
        return self.pal_list

    def find_palin_one(self,pair):
        newpair=pair
        newpair.append(pair[0])
        if self.check_palindrome(newpair):
            self.pal_list.append(pair[0])

    def find_palin_pairs(self,pair):
        if self.check_palindrome(pair):
            tup=(pair[0],pair[1])
            self.pal_list.append(tup)

    def check_palindrome(self,word):
        first=word[0]
        revsec=word[1][::-1]
        if first==revsec:
            return True

obj=PalResult()
result=obj.group_palin(words)
print(result)

#redo with itertools.combination

#optimize with nested for loop without inbuilt libs