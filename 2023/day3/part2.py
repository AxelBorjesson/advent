def dotmatrix():
    dot_matrix = []
    inter_list = []
    with open("input.txt","r") as text_file:
        lines = text_file.read().splitlines()
    for line in lines:
        inter_list = []
        for c in line:
            inter_list.append(c)
        dot_matrix.append(inter_list)
    return dot_matrix

def find():
    matrix = dotmatrix()
    pos= []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "*":
                pos.append(f"{i} {j}")
    
    return pos
               
def numbersearch():
    matrix = dotmatrix()
    pos = find()
    inter_list = []
    fina_list = []
    for element in pos:
        inter_list = []
        i = int(element.split()[0])
        j = int(element.split()[1])
        for n in range(max(i-1,0),min(i+2,len(matrix)),1):
            for p in range(max(0,j-1),min(j+2,len(matrix[0])),1):
                if matrix[n][p].isnumeric():
                    if not matrix[n][p+1].isnumeric() or p == len(matrix[0])-1:
                        if not [n, p] in inter_list:
                            inter_list.append([n, p])
                    elif matrix[n][p+1].isnumeric() and (not matrix[n][p+2].isnumeric() or p+1 ==len(matrix)-1):
                        if not [n, p+1] in inter_list:
                            inter_list.append([n, p+1])
                    else:
                        if not [n, p+2] in inter_list:
                            inter_list.append([n, p+2])
        if len(inter_list) == 2:
            fina_list.extend(inter_list)
    
    return fina_list
    
def numlen(i,j):
    matrix = dotmatrix()
    if not matrix[i][j-1].isnumeric():
        return 0
    elif not matrix[i][j-2].isnumeric():
        return 1
    else:
        return 2   
                    
def multitime():
    pos = numbersearch()
    matrix = dotmatrix()
    adding_value = 0
    for i in range(1,len(pos),2):
        leng2 = numlen(pos[i][0],pos[i][1])
        leng1 = numlen(pos[i-1][0],pos[i-1][1])
        i1 = pos[i-1][0]
        i2 = pos[i][0]
        j1 = pos[i-1][1]
        j2 = pos[i][1]
        num1 = int("".join(matrix[i1][j1-leng1:j1+1]))
        num2 = int("".join(matrix[i2][j2-leng2:j2+1]))
        adding_value += num1*num2
    print(adding_value)
       



multitime()
