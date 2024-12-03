def one():
    with open("day2/test.txt","r") as text_file:
        reports = text_file.read().splitlines()

    safes = 0
    for report in reports:
        wow = report.split()
        print(wow)
one()
