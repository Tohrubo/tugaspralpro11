handle = open("mbox-short.txt", "r")

lines = handle.readlines()
d = {}
for line in lines:
    sentence = line.split()
    for word in sentence:
        if ":" in word and word[0].isdigit():
            numlst = word.split(":")
            if len(numlst[0]) <= 2:
                hour = numlst[0]
                d[hour] = d.get(hour, 0) + 1

lst = []
for key, val in d.items():
    lst.append((key, val))
lst.sort()

for i in range(len(lst)):
    print(lst[i][0], lst[i][1])

handle.close()