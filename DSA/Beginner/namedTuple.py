import collections

personType=collections.namedtuple('person',['fname','lname','country'])
emp1=personType("jon","mike",'usa')
emp2=personType("peter","mark","canada")
emp3=personType("jerry","smith","mexico")
print(emp1[0]) #jon
print(emp1.fname) #jon
emplist=[]
emplist.append(emp1)
emplist.append(emp2)
emplist.append(emp3)
print(emplist)

print(emplist.fname)