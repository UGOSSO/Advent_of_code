Input = open("data.txt", "r")
values = Input.read()
Input.close()

list_of_values = list(map(str, values.split("\n")))

#Part I 
def power_comp(L) :
    temp = [[0, 0] for i in range(len(L[0]))]
    gamma = "0b"
    epsilon = "0b"

    for i in L :
        for  j in range(len(i)) :
            if i[j] == "1" : temp[j][1]+=1
            else : temp[j][0]+=1

    for i in temp :
        gamma+= "1" if max(i) == i[1] else "0"
        epsilon+= "1" if min(i) == i[1] else "0"
    
    dec_gamma = int(gamma, 2)
    dec_epsilon = int(epsilon, 2)

    return dec_epsilon*dec_gamma