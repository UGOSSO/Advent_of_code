Input = open("data.txt", "r")
value = Input.read()
Input.close()

list_values = list(map(int, value.split(" ").split("\n")))

#work for part I and II
def poisson(L) :
    #create a lsit with the number of day possible 
    x = [0 for i in range(9)] 
    
    for i in range(9) : 
        #count how much fish there is in each day
        x[i] = L.count(i)
    
    for i in range(256) :
        #each day make the fish of each day goes into the day after and add the new fish 
        x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8] = x[1], x[2], x[3], x[4], x[5], x[6], x[7]+x[0], x[8], x[0]
    
    return sum(x)