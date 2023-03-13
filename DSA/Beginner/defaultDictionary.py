import collections

def def_user_value():
    return "empty"
dd=collections.defaultdict(list)
print(dd)

l=["abc","acb","bcd","cde"]

# print(sorted("anc"))
for i in l:
    dd["".join(sorted(i))].append(i)
print(dd)

# -----------
dd1=collections.defaultdict(def_user_value)
print(dd1)

dd1["a"]=1
dd1["b"]=2

print(dd1)
print(dd1["c"]) #empty

d={"a":1,"b":2}
print(d["a"])
print(d["c"]) #KeyError: 'c'
