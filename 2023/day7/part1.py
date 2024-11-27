def one():
    fullrank = []
    indlist = ["A","K","Q","J","T","9","8","7","6","5","4","3","2","1"]
    fives = []
    fours = []
    fulls = []
    threes = []
    tpairs = []
    pairs = []
    high = []
    megamatrix =[
        fives,
        fours,
        fulls,
        threes,
        tpairs,
        pairs,
        high,
    ]  
    with open("test.txt","r") as text_file:
        lines = text_file.read().splitlines()
    for line in lines:
        cards = []
        hand, bid = line.split()
        tie = ""
        for k in range(5):
            tie = tie + f"{indlist.index(hand[k])} "
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
        elif cards == [1]:
            pairs.append(inter)
        else:
            high.append(inter)
    for matrix in megamatrix:
        if matrix != []:
            fullrank.extend(tiebreaker(matrix))
    return fullrank


def tiebreaker(matrix):
    
    return matrix


        
            
               
            

            
            


        
        

one()