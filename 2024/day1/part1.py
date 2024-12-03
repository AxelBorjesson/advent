def one():
    flist = []
    llist = []
    distance = 0
    with open("day1/puzzle.txt","r") as text_file:
        lines = text_file.read().splitlines()

    for line in lines:
        l1,l2 = line.split()
        flist.append(int(l1))
        llist.append(int(l2))
    flist.sort()
    llist.sort()
    for i in range(len(flist)):
        if flist[i] >= llist[i]:
            distance += flist[i]-llist[i]
        else:
            distance+= llist[i]-flist[i]
    print(distance)


one()