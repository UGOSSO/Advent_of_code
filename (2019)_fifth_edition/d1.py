Input = open("./data/2019/data1.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(map(int, values.split("\n")))

#Part I
def fuel_CU(L) :
    #return the sum of each mass//3-2
    return sum([i//3-2 for i in L])

#Part II 
def fuel__for_fuel(L) :
    base = [i//3-2 for i in L]
    res = 0

    #for each mass
    for i in range(len(base)) :
        #add to the res the fuel needed for the mass and for the fuel needed until the fuel needed don't need more fuel 
        while base[i] > 0 :
            res+=base[i]
            base[i] = base[i]//3-2

    return res

# print(fuel_CU(list_of_values)) #-> Part I
# print(fuel__for_fuel(list_of_values)) #-> Part II