
def listshift(flist):
    flist = flist[1:]
    flist.append(1)

    return flist

    



def two():
    futlist = [1,1,1,1,1,1,1,1,1,1,1]
    with open("test.txt","r") as text_file:
        cardlist = text_file.read().splitlines()
    total_value = 0
    for card in cardlist:
        futlist = listshift(futlist)
        card_won = 0
        card = card[7:]
        card = sorted(card.split())[:-1]
        print(card)
        for i in range(1,len(card),1):
            if card[i] == card[i-1]:
               card_won += 1
        for i in range(1,card_won+1,1):
            futlist[i] += 1*futlist[0]
        total_value +=futlist[0]
        
    
    return total_value
    


 
    
print(two())