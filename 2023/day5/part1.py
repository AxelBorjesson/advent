#destination range start, source range start, range length
#seed-to-soil: seed = source, soil = location.

def one():
    with open("input.txt","r") as text_file:
        text = text_file.read().splitlines()
    listindex = 0
    seeds = text[0].split(":")[1].split()
    lowloc = 0
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
    for seed in seeds:
       location = rangefinder(0,int(seed),megamatrix)
       if lowloc == 0:
           lowloc = location
       elif location < lowloc:
           lowloc = location

    return lowloc    
  
       
        



def rangefinder(map,source,matrix):
    if map == 7:
        return source
    for i in range(len(matrix[map])):
        if int(matrix[map][i][1]) <= source < int(matrix[map][i][1]) + int(matrix[map][i][2]):
            shift = source - int(matrix[map][i][1])
            newsource = shift + int(matrix[map][i][0])
            return rangefinder(map+1,newsource,matrix)
    return rangefinder(map+1,source,matrix)

        
                    
    
    

  


    
    
    
    
        





    


print(one())