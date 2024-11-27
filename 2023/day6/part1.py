def one():
    inlist = []
    with open("input.txt","r") as text_file:
        distime = text_file.read().splitlines()
    for time in distime:
        inlist.append(time.split())
    inlist[0].pop(0)
    inlist[1].pop(0)
    racelist = []
    for i in range(len(inlist[0])):
        racelist.append([int(inlist[0][i]),int(inlist[1][i])])
    
    multi = 0
    for race in racelist:
        omax = False
        counter = 0
        if race[0] % 2 == 0:
            maxima = int(race[0]/2)
            omax = True
        else:
            maxima = int(race[0]/2 + 0.5)
        for x in range(maxima,race[0]):
            y = x*race[0] - x**2
            if y > race[1]:
                counter += 1
            else:
                break
        counter = counter*2
        if omax:
            counter -=1
        if multi == 0:
            multi = counter
        else: multi = multi*counter
    
    return multi


   




print(one())