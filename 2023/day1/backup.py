def lmao():
    framdic = {"one": 1,"two":2,"three": 3, "four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    bakdic = {"eno":1,"owt":2,"eerht":3,"ruof":4,"evif":5,"xis":6,"neves":7,"thgie":8,"enin":9}
    adding_sum = 0
    with open("cal.txt","r") as text_file:
        lines = text_file.read().splitlines()
    for shit in lines:
        first = 0
        last = 0
        for i in range(len(shit)-1,-1,-1):
            if shit[i].isnumeric():
                last += int(shit[i])
                break
        for i in range(len(shit)):
            if shit[i].isnumeric():
                first += int(shit[i])
                print(str(first)+str(last))
                adding_sum += int(str(first)+str(last))
                break
    
    return adding_sum
print(lmao())