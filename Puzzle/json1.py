'''
Input - [{"emp_id":100,"name":"Apple"},{"emp_id":101,"name":"Ball"},{"emp_id":100,"name":"Apple"},
        {"emp_id":100,"name":"Apple"}, {"emp_id":100,"name":"Apple", "contact":123}, {"id":100,"name":"Apple"}]

Output - [{"emp_id":100,"name":"Apple", "frequency":3},{"emp_id":101,"name":"Ball","frequency": 1},
            {"emp_id":100,"name":"Apple", "contact":123, "frequency":1}, {"id":100,"name":"Apple", "frequency":1}]
There could be any number of keys and no keys are fixed, for eg - emp_id won't be present
in all dictionary and even a single key difference will be a different dictionary```

'''
import json

# import CONFIG as CONFIG
import sha256

Input = """[{"emp_id":100,"name":"Apple"},{"emp_id":101,"name":"Ball"},{"emp_id":100,"name":"Apple"},{"emp_id":100,"name":"Apple"},{"emp_id":100,"name":"Apple", "contact":123},{"id":100,"name":"Apple"}]"""

# hashing scenario
# serialize and deserialize
'''
unique key, [{actual content}, frequency]

'''

# class IP:
#
#
#     def __init__(self):
#         self.emp_id
#         self.

d={}
IP=json.loads(Input)
print(IP)
n=len(IP)
print(n)
for i in range(n):
    print(type(IP[i]))
    print(IP[i])
    print(len(IP[i]))
    '''
     check if the len of incoming and existing item is same for same
      
    '''
    # try:
    #     if IP[i]['emp_id']:
    #         print(IP[i]['emp_id'])
    # except:
    #     print("An exception occurred")


    # hashKey=hash(IP[i]['emp_id'])
    # print(hashKey)
    # DIGEST = sha256(json.dumps(CONFIG.__dict__, sort_keys=True).encode('utf8')).hexdigest()
    if IP[i] in d:
        d[IP[i]]+=1
    else:
        d[IP[i]]=1




