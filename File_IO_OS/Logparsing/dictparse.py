# dict = {'name': "name", 'Name': "Name", 'nam': "nam"}
# list = ['name','nam']

# for i in list:
#     if i in dict:
#         print(dict[i])

# print([key.lower() for key in dict.keys()])
# print(map(str.lower(),dict.keys())) #not working
# for i in list:
#     if i.lower() in [key.lower() for key in dict.keys()]:
#         print(dict[i])

ldict=[{'name': "name1", 'host': "host1"},
       {'Name': "Name2", 'host': "host2Name"},
       {'nam': "nam3",   'host': "host3nam"},
       {'name': "name4", 'host': "host4"}]

list = ['name','nam']

# for i in range(len(ldict)):
#     d=ldict[i]
#     print([key.lower() for key in d.keys()])

# for i in range(len(ldict)):
#     d=ldict[i]
#     for l in list:
#         if l.lower() in [key.lower() for key in d.keys()]:
#             print(d[l])

#print all values of name
for i in range(len(ldict)):
    d=ldict[i]
    for l in list:
        if l in d.keys():
            print(d[l])




