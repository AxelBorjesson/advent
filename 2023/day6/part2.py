def one():
    inlist = []
    race = []
    with open("day6/input.txt","r") as text_file:
        distime = text_file.read().splitlines()
    for time in distime:
        inlist.append(time.split())
    inlist[0].pop(0)
    inlist[1].pop(0)
    race.append(int("".join(inlist[0])))
    race.append(int("".join(inlist[1])))
   
   
   
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
    return counter



print(one())