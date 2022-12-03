Input = open("./data/2021/data3.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(map(str, values.split("\n")))

#Part I 
def power_comp(L) :
    """
        input : L is a list of binary strings
        output : the product between epsilon and gamma 
    """

    temp = [[0, 0] for i in range(len(L[0]))]
    gamma = "0b"
    epsilon = "0b"

    #create a list which stock for each bit the occurences of 0 and 1 present in the list
    for i in L :
        for  j in range(len(i)) :
            if i[j] == "1" : temp[j][1]+=1
            else : temp[j][0]+=1

    #for each bit add the max occurence to gamma and the min to epsilon 
    for i in temp :
        gamma+= "1" if max(i) == i[1] else "0"
        epsilon+= "1" if gamma == "0" else "0"
    
    #transform gamma and epsilon into integer 
    dec_gamma = int(gamma, 2)
    dec_epsilon = int(epsilon, 2)

    return dec_epsilon*dec_gamma

#Part II

def distrib(L, index) :
    """
        input : L is a list of binary strings, index is an integer > 0 and < len(L[i])
        output : compute a list which stock the occurences of 0 and 1 for the given bit
    """
    
    temp = [0, 0]
    
    for i in L : 
        if i[index] == "1" : temp[1]+=1
        else : temp[0]+=1

    return temp

def sol(index, distrib_most, distrib_least, most, least) :
    """
        input : 
        most is a list of binary string
        least is a list od a binary string
        index is an integer within the range of the binary in the list most and least 
        distrib_most and distrib_least is the value of the distrib function define before for the given index 
        
        output : the product between oxygen_rates and co2_rates  
    """

    #give the the present bit for the given index in most and the least present for the given index in least 
    is_most = "1" if max(distrib_most) == distrib_most[1] else "0" 
    is_least = "0" if min(distrib_least) == distrib_least[0] else "1"

    #check if most is composed of more than 1 binary 
    if len(most) > 1 :
        #change most to the list of the binary which are composed of the is_most bit for the given index 
        temp = []
        for i in most :
            if i[index] == is_most :
                temp.append(i)
        most = temp
    #check if least is composed of more than 1 binary 
    if len(least) > 1 :
        #change least to the list of the binary which are composed of the is_least bit for the given index 
        temp = []
        for i in least :
            if i[index] == is_least :
                temp.append(i)
        least = temp

    #if most or least are composed of more than one binary, make a recursive call of the function with an increase of the index by 1 
    if len(least) > 1 or len(most) > 1 :
        return sol(index+1, distrib(most, index+1), distrib(least, index+1), most, least)
    #compute the integer values of ox and co and return the product  
    else : 
        ox = int("0b" + most[0], 2)
        co = int("0b" + least[0], 2)
        return ox*co
            
def ox_co(L) :
    """
        input : L is a list of binary strings 
        output : call the sol function that return the needed product
    """

    #create the first distribution for the call 
    temp = distrib(L, 0)
    return sol(0, temp, temp, L, L)

# print(power_comp(list_of_values)) #-> Part I
# print(ox_co(list_of_values)) #-> Part II