
def one():
    with open("input.txt","r") as text_file:
        text = text_file.read().splitlines()
    listindex = 0
    seeds = text[0].split(":")[1].split()
    seedlist = []
    megamatrix = [
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    for i in  range(2,len(text),1):
        if text[i] == "":
            listindex += 1
        elif text[i][0].isnumeric():
            megamatrix[listindex].append(text[i].split())
    for j in range(len(megamatrix)):
        for k in range(len(megamatrix[j])):
            megamatrix[j][k][0], megamatrix[j][k][1] = int(megamatrix[j][k][1]), int(megamatrix[j][k][0])
        megamatrix[j] = sorted(megamatrix[j])
    
    for p in range(1,len(seeds),2):
        oneseed = [int(seeds[p-1]), int(seeds[p]) + int(seeds[p-1])-1]
        seedlist.append(oneseed)
    lowlocs = seedsave(seedlist,megamatrix)
    lowlocs.sort()
    return lowlocs[0][0]
    
   

def seedsave (seeds,matrix):
    currentmap = seeds
    nextmap = []
    mapcounter = 0
    while currentmap:
        nextmap.extend(recur(currentmap.pop(),matrix[mapcounter]))
        if currentmap == []:
            print(mapcounter)
            mapcounter += 1
            if mapcounter == 7:
                return nextmap
            else:
                currentmap = nextmap
                nextmap = []

                

def recur(seed, matrix):
    startlist = [int(x[0]) for x in matrix]
    seedstart = seed[0]
    seedend = seed[1]
    offsets = []
    startlist.append(startlist[-1]+int(matrix[-1][2]))
    #finding indecies for seedstart and seedend
  
    if seedstart >= startlist[-1]:
        sind = len(startlist)
    else:
         for i in range(len(startlist)):
            if seedstart < startlist[i]:
                sind = i
                break
    if seedend < startlist[0]:
        eind = 0
    else:
        for j in range(len(startlist)-1,-1,-1):
            if seedend >= startlist[j]:
                eind = j+1
                break        
    
    #find amount of seeds to return aswell as what offsets to use
    if sind == eind:
        if sind == 0 or sind == len(startlist):
            offsets.append(0)
        else:
            offsets.append(int(matrix[sind-1][1]) - int(matrix[sind-1][0]))
    else:
        if sind == 0:
            offsets.append(0)
        for p in range(max(sind,1),min(len(startlist),eind+1),1):
            offsets.append(int(matrix[p-1][1]) - int(matrix[p-1][0]))
        if eind == len(startlist):
            offsets.append(0)
    
    # find and return seeds
    inter_seed = []
    seedlist = []
    if len(offsets) == 1:
        inter_seed.append(seedstart + offsets[0])
        inter_seed.append(seedend + offsets[0])
        seedlist.append(inter_seed)
        inter_seed = []

    else:
        if offsets[0] == 0:
            offsets.pop(0)
            inter_seed.append(seedstart)
            inter_seed.append(startlist[0]-1)
            seedlist.append(inter_seed)
            inter_seed = []
            seedstart = startlist[0]
        if offsets[-1] == 0:
            offsets.pop(-1)
            inter_seed.append(startlist[-1]+int(matrix[-1][2]))
            inter_seed.append(seedend)
            seedlist.append(inter_seed)
            inter_seed =[]
            seedend = startlist[-1]+int(matrix[-1][2])-1
        
        for k in range(len(startlist)-1):
            if startlist[k] <= seedstart < startlist[k+1]:
                if seedend < startlist[k+1]:
                    inter_seed.append(seedstart + offsets[0])
                    inter_seed.append(seedend + offsets.pop(0))
                    seedlist.append(inter_seed)
                    inter_seed = []
                else:
                    inter_seed.append(seedstart+ offsets[0])
                    inter_seed.append(startlist[k+1]-1 + offsets.pop(0))
                    seedlist.append(inter_seed)
                    inter_seed = []
                    seedstart = startlist[k+1]
            if offsets == []:
                break
    
    return seedlist


 
    

       

        


            

            

    
   


           
print(one())
