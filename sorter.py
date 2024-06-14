fin = open("./unsorted.txt")
fout = open("./sorted.txt", "w")

group = []

for ind in fin:
    fname = ""
    sname = ""
    name = ""
    reqs = False
    if "(REQS)" in ind:
        ind = ind[:-6]
        reqs = True
    beforeComma = True
    for c in ind:
        if c == ",":
            beforeComma = False
        if beforeComma:
            sname += c
        else:
            fname += c

    fname = fname[2:]
    fname = fname[:-1]
    fname = fname.strip()
    sname = sname.strip()
    name = fname + " " + sname
    if reqs:
        print("Adding (REQS)")
        name += " (REQS)"
        print(name)
    group.append(name)

group.sort()
for g in group:
#    print(g)
    fout.write(g + "\n")

fin.close()
fout.close()