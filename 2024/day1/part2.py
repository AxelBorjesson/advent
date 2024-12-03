def one():
    flist = []
    llist = []
    sim_score = 0
    with open("day1/puzzle.txt","r") as text_file:
        lines = text_file.read().splitlines()

    for line in lines:
        l1,l2 = line.split()
        flist.append(int(l1))
        llist.append(int(l2))
    for i in range(len(flist)):
       sim_score += flist[i] *llist.count(flist[i])
    print(sim_score)


one()