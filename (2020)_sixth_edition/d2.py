Input = open("./data/2020/data2.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(i.split(" ") for i in list(map(str, values.split('\n'))))

#work for part I and part II
def valid(L) :
    res_partI = 0 
    res_partII = 0
    res = 0

    for i in L :
        #transform the "x-y" in [int(x), int(y)] for the range line 18 and the equality test line 21 
        i[0] = list(map(int, i[0].split("-")))

        #check the rule that make the password valid for the part I and if the rule is respected add 1 to the counter 
        if (i[2].count(i[1][0]) in range(i[0][0], i[0][1]+1)) : res_partI+=1

        #check the rule that make the password valid for the part II and if the rule is respected add 1 to the counter
        if (i[2][i[0][0]-1] == i[1][0] and i[2][i[0][1]-1] != i[1][0]) or (i[2][i[0][0]-1] != i[1][0] and i[2][i[0][1]-1] == i[1][0]) : res_partII+=1

    return res_partI, res_partII 

# print(valid(list_of_values))