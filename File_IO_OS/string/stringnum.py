st="harsh95"

for t in range(len(st)):
    if not st[t].isalpha():
        num = int(st[t:])
        print(num)
        continue
    print("done")
