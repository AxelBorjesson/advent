def possible():
    adding_sum = 0
    with open("input.txt","r") as text_file:
        gamelist = text_file.read().splitlines()
    for i,game in enumerate(gamelist):
        min_blue = 0
        min_red = 0
        min_green = 0
        game = game[7 +len(str(i+1)):].split(";")
        for set in game:
            setlist = set.split(",")
            for colourbag in setlist:
                final = colourbag.split()
                if final[1] == "blue" and int(final[0]) > int(min_blue):
                    min_blue = int(final[0])
                elif final[1] == "green" and int(final[0]) > int(min_green):
                    min_green = int(final[0])
                elif final[1] == "red" and int(final[0]) > int(min_red):
                    min_red = int(final[0])
        adding_sum += min_green*min_blue*min_red
      
             
    return adding_sum

                    


              



print(possible())