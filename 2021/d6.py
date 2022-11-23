Input = open("data.txt", "r")
value = Input.read()
Input.close()

#transform the input in a usable data structure
list_values = list(map(int, value.split(" ").split("\n")))

#work for part I and II
def poisson(L, number_of_day) :
    """
        input : 
        L is a list of integer between 0 and 8, each integer represent a fish and is value represent the number of day before the reproduction
        number_of_day : the number of day before we check the results
        
        output : the number of fish after number_of_day days
    """

    #create a lsit with the number of day possible 
    x = [0 for i in range(9)] 
    
    for i in range(9) : 
        #count how much fish there is in each day
        x[i] = L.count(i)
    
    for i in range(number_of_day) :
        #each day make the fish of each day goes into the day after and add the new fish 
        x = x[1], x[2], x[3], x[4], x[5], x[6], x[7]+x[0], x[8], x[0]
    
    return sum(x)