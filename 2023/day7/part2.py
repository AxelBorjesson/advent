def one():
    adding_value = 0
    fullrank = []
    indlist = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"]
    indlist2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]
    fives = []
    fours = []
    fulls = []
    threes = []
    tpairs = []
    pairs = []
    high = []
    megamatrix =[
        high,
        pairs,
        tpairs,
        threes,
        fulls,
        fours,
        fives,
    ]  
    with open("day7/input.txt","r") as text_file:
        lines = text_file.read().splitlines()
    for line in lines:
        cards = []
        hand, bid = line.split()
        tie = ""
        for k in range(5):
            tie = tie + indlist2[indlist.index(hand[k])]
        inter = [tie, hand, bid]
        for ind in indlist:
           p = hand.count(ind)
           if p > 1:
               cards.append(p)
        if cards == [5]:
            fives.append(inter)
        elif cards == [4]:
            fours.append(inter)
        elif cards == [3,2] or cards == [2,3]:
            fulls.append(inter)
        elif cards == [3]:
            threes.append(inter)
        elif cards == [2,2]:
            tpairs.append(inter)
        elif cards == [2]:
            pairs.append(inter)
        else:
            high.append(inter)
    for matrix in megamatrix:
        if matrix != []:
            fullrank.extend(tiebreaker(matrix))
    print(fullrank)
    for r in range(len(fullrank)):
        adding_value += int(fullrank[r][2])*(r+1)
    return adding_value


    





def tiebreaker(matrix):
    matrix.sort(reverse= True)
    return matrix


        
            
               
            

            
            


        
        

print(one())