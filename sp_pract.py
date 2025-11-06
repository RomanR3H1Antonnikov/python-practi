sp1 = [1, 2, 3, 4, 5, 6, 7]
sp2 = [1, 2, 3, 4]
sp3 = []
maxsp = max(sp1, sp2)
for i in range(0, max(len(sp1), len(sp2))):
    if i < len(min(sp1, sp2)):
        sp3.append(max(sp1, sp2)[i] + min(sp1, sp2)[i])
    else:
        sp3.append(maxsp[i])
print(sp3)