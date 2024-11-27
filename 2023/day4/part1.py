def one():
    with open("input.txt","r") as text_file:
        cardlist = text_file.read().splitlines()
    total_value = 0
    for card in cardlist:
        card_value = 0
        card= card[7:]
        winum = card.split("|")
        carnum = winum[1].split()
        winum = winum[0].split()
        for num in winum:
            if num in carnum:
                if card_value == 0:
                    card_value = 1
                else:
                    card_value *= 2
        total_value += card_value
    
    return total_value



def two():
    with open("test.txt","r") as text_file:
        cardlist = text_file.read().splitlines()
    total_value = 0
    for card in cardlist:
        card_value = 0
        card = card[7:]
        card = sorted(card.split())[:-1]
        for i in range(1,len(card),1):
            if card[i] == card[i-1]:
                if card_value == 0:
                    card_value = 1
                else:
                    card_value *= 2
        total_value += card_value

    return total_value        
        
            
    






print(one())
print(two())