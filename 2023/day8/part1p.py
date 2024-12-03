def one():
    with open("day8/puzzle.txt","r") as text_file:
        maps = text_file.read().splitlines()
    turns = maps[0]
    current = "AAA"
    maps = maps[2:]
    maplist = []
    cur = []
    for map in maps:
        loc, next = map.split("= ")
        loc = loc[:-1]
        next = next[1:-1]
        nl,nr = next.split(",")
        nr = nr.strip()
        fmap = [nl,nr]
        cur.append(loc)
        maplist.append(fmap)
    ind = 0
    steps = 0
    while current != "ZZZ":
        if ind == len(turns):
            ind = 0
        if turns[ind] == "L":
           current = maplist[cur.index(current)][0]
        else:
            current = maplist[cur.index(current)][1]
        ind +=1
        steps+=1
        if steps == 50000:
            break
    print(steps)        
        
         
       


one()