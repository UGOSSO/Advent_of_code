Input = open("./data/2022/data10.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(map(str, values.split('\n')))

def strenght(L) :
    res, nb_cycle = 1, 0 
    val = []

    for i in L : 
        #if it's a noop 
        if i == 'noop' :
            nb_cycle+=1
        
        #if it's an add
        if 'addx' in i : 
            #take the value of the add 
            temp = int(list(map(str, i.split(' ')))[1])
            
            #add the cycle of the add then check if we passed a intereseting cycle 
            nb_cycle+=2
            #if an add finish on cycle 20 the value is here for cycle 21 not 20 so we test before append 
            if nb_cycle == 20 or nb_cycle == 60 or nb_cycle == 100 or nb_cycle == 140 or nb_cycle == 180 or nb_cycle == 220 :
                val.append(res*nb_cycle)
            
            #append the value of add
            res+=temp
        
        #since we check in the add for cycle 20, 60 ... we need to check for the noop here 
        if i == 'noop' and (nb_cycle == 20 or nb_cycle == 60 or nb_cycle == 100 or nb_cycle == 140 or nb_cycle == 180 or nb_cycle == 220) :
            val.append(res*nb_cycle)
        
        #if the add is for the 19th cycle we will finish it on cycle 21 so we need to check for them to and if it's the case we append the value before the last cycle
        if 'addx' in i and (nb_cycle == 21 or nb_cycle == 61 or nb_cycle == 101 or nb_cycle == 141 or nb_cycle == 181 or nb_cycle == 221) :
            val.append((res-temp)*(nb_cycle-1))

    #we return the sum of the values 
    return sum(val)

def sprite(L) :
    res, nb_cycle = 1, 0 
    val, sprite_pos = [], []
    draw = ''

    #we take all values for each cycle
    for i in L : 
        #if it's a noop
        if i == 'noop' :
            nb_cycle+=1
            val.append(res)
        
        #if it's an add 
        if 'addx' in i : 
            #take the value of the add 
            temp = int(list(map(str, i.split(' ')))[1])
            #two cycle in a add so we append two time 
            val.append(res)
            val.append(res)
            #after (for the same reason as before) append we set the new values of register
            res+=temp

    #for each cycle
    for i in range(1, len(val)+1) : 
        #we get the sprite value
        sprite_pos.append([val[i-1], val[i-1]+1, val[i-1]+2]) 
        
        #if the cycle value is in the sprite value draw a #
        if i%40 in sprite_pos[-1] : draw+='#'
        #else draw a .
        else : draw+='.'
        #every 40 cycle we go to the line 
        if i % 40 == 0 : draw+='\n'

    return draw

# print(strenght(list_of_values)) #-> Part I
# print(sprite(list_of_values)) #-> Part II