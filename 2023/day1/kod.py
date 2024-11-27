def lmao():
    framdic = {"one": 1,"two":2,"three": 3, "four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    bakdic = {"eno":1,"owt":2,"eerht":3,"ruof":4,"evif":5,"xis":6,"neves":7,"thgie":8,"enin":9}
    adding_sum = 0
    with open("cal.txt","r") as text_file:
        lines = text_file.read().splitlines()
    for shit in lines:
        work_word = ""
        work_word2 = ""
        first = 0
        last = 0
        for i in range(len(shit)-1,-1,-1):
            work_word2 = work_word2 +shit[i]
            if work_word2[-3:] in bakdic:
                last = bakdic[work_word2[-3:]]
                work_word2 = ""
                break
            elif work_word2[-4:] in bakdic:
                last = bakdic[work_word2[-4:]]
                work_word2 = ""
                break   
            elif work_word2[-5:] in bakdic:
                last = bakdic[work_word2[-5:]]
                work_word2 = ""
                break
            elif shit[i].isnumeric():
                last += int(shit[i])
                break
        for i in range(len(shit)):
            work_word = work_word + shit[i]
            if work_word[-3:] in framdic:
                first = framdic[work_word[-3:]]
                break
            elif work_word[-4:] in framdic:
                first = framdic[work_word[-4:]]
                break
            elif work_word[-5:] in framdic:
                first = framdic[work_word[-5:]]
                break
            elif shit[i].isnumeric():
                first += int(shit[i])
                break
        print(str(first)+str(last))
        adding_sum += int(str(first)+str(last))
    
    return adding_sum
print(lmao())