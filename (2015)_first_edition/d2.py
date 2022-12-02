Input = open("./data/2015/data2.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(i.split("x") for i in list(map(str, values.split("\n"))))

#Part I 
def paper(L) :
    res = 0

    #we calculate the size of each side, transform the list of list ['l', 'w', 'h'] in list of [a = l*w, b = w*h, c = h*l]
    temp = [[int(j[0])*int(j[1]), int(j[1])*int(j[2]), int(j[2])*int(j[0])] for j in L]

    for i in temp :
        #2*sum(i) for (2*a+2*b+2*c) and min(i) for the smallest side because we already calculated their value at line 13
        res+=(2*sum(i)+min(i))

    return res 

#Part II
def ribbon(L) :
    res = 0

    #we tranform each lenght in an integer 
    temp = [[int(j[0]), int(j[1]), int(j[2])] for j in L]

    for i in temp :
        #2*sum(sorted(i)[:2]) for the smallest perimeter and (i[0]*i[1]*i[2]) for l*w*h
        res+=(2*sum(sorted(i)[:2])+(i[0]*i[1]*i[2]))

    return res

# print(paper(list_of_values)) -> Part I
# print(ribbon(list_of_values)) -> Part Ii