Input = open("./data/2022/data4.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
#can be treated in one line but f*cking unreadable
list_of_values = list(map(str, values.split("\n")))
list_of_values = list(list(map(str, i.split(","))) for i in list_of_values)
list_of_values = list([list(map(int, i[0].split("-"))), list(map(int, i[1].split("-")))] for i in list_of_values)
list_of_values = list([list(range(i[0][0], i[0][1]+1)), list(range(i[1][0], i[1][1]+1))] for i in list_of_values)

#Part I
def in_another(L) :
    res = 0 

    for j in L :
        #check both inclusion with first and last term
        if (j[0][0] <= j[1][0] and j[0][-1] >= j[1][-1]) or (j[0][0] >= j[1][0] and j[0][-1] <= j[1][-1]) : res += 1

    return res 

#Part II
def overlap(L) :
    res = 0 
    
    for j in L :
        #if the first elt or the last elt of one list is in another then the assignments are overlapping
        #we don't do the test in one line to optimize a little but it is totally sustainable
        if j[0][0] in j[1] or j[0][-1] in j[1] :
            res+=1
        else : 
            if j[1][0] in j[0] or j[1][-1] in j[0] : res+=1

    return res

# print(in_another(list_of_values))  #-> Part I
# print(overlap(list_of_values)) #-> Part II
