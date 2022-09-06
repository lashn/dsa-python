import re
# txt="""27.59.104.166 - - [04/Oct/2019:21:15:54 +0000] "GET /users/login HTTP/1.1" 200 41716 "-" "okhttp/3.12.1"""
#
# pat=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
#
# obj=re.compile(pat)
# print(obj.match(txt))

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
pat=re.compile(r'\d\d\d')

# with open("log.txt",'r') as fobj:
#     rline=fobj.readlines()
#     for line in rline:
#         ans=pat.findall(line)
#         print(ans)

pat= r'\d'
# pat=r'[a-z0-9]+@[a-z]+\.[a-z]{2,3}' #email
# pat=r'\d{3}-\d{3}-\d{4}'
ans=re.findall(pat,"log.txt")
print(ans)




