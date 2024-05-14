tA = (90, 90, 90, 90, 90)
same = True


chk = tA[0]
for item in tA:
    if chk == item:
        continue
    else:
        same = False
        break


print(same)