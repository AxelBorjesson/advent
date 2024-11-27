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

def findnumbers(dotmatrix):
    adding_list = []
    for i in range(len(dotmatrix)):
        for j in range(len(dotmatrix)):
            if dotmatrix[i][j].isnumeric() and (j == len(dotmatrix[i]) - 1 or not dotmatrix[i][j+1].isnumeric()):
                numlen = numberleng(dotmatrix,i,j)
                jstart = max(j - numlen+1,0)
                if symbolsearch(dotmatrix, i , jstart-1, min(j+2,len(dotmatrix[0]))):
                    inter_word = "".join(dotmatrix[i][jstart:j+1])
                    print(inter_word)
                    adding_list.append(int(inter_word))
                    

    return(sum(adding_list))            
                    




def numberleng(dotmatrix, i,j):
    if not dotmatrix[i][j-1].isnumeric():
        return 1
    elif not dotmatrix[i][j-2].isnumeric():
        return 2
    else:
        return 3

def symbolsearch(dotmatrix, i, js,je):
    for r in range(max(i-1,0),min(i+2,len(dotmatrix)),1):
        for j in range(js,je,1):
            if not dotmatrix[r][j].isnumeric() and not dotmatrix[r][j] == ".":
                return True
    return False


    





       


print(findnumbers(dotmatrix()))