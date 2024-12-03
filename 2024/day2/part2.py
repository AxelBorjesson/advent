def one():
    with open("day2/puzzle.txt","r") as text_file:
        reports = text_file.read().splitlines()

    safes = 0
    for report in reports:
       report = report.split()
       safes += safesearch(report)
    return safes


def safesearch(report):
    x = incdec(report)
    if x == 0:
        return 0
    for i in range(len(report)-1):
        if int(report[i]) - int(report[i+1]) not in x:
            if skiptest(report,x):
                return 1
            else:
                return 0

    return 1

def skiptest(report,x):
    for i in range(len(report)):
        skip = report.copy()
        skip.pop(i)
        for j in range(len(skip)-1):
            if int(skip[j]) - int(skip[j+1]) not in x:
                break
        else:
            return True
    return False




            
            


def incdec(report):
    inc = 0
    dec = 0
    for i in range(len(report)-1):
        if int(report[i]) - int(report[i+1]) < 0:
            inc +=1
        elif int(report[i]) -int(report[i+1]) > 0:
            dec +=1
    if inc < dec:
        return [1,2,3]
    elif dec < inc:
        return [-1,-2,-3]
    else:
        return 0

        
print(one())   