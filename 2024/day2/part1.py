def one():
    with open("day2/puzzle.txt","r") as text_file:
        reports = text_file.read().splitlines()

    safes = 0
    for report in reports:
       report = report.split()
       safes += safesearch(report)
    return safes


def safesearch(report):
    inc =[1,2,3]
    dec = [-1,-2,-3]
    if int(report[0]) - int(report[1]) in inc:
        x=inc
    elif int(report[0]) - int(report[1]) in dec:
        x=dec
    else:
        return 0
    for i in range(len(report)-1):
        if int(report[i]) - int(report[i+1]) not in x:
            return 0
    print(report)
    return 1
        


print(one())