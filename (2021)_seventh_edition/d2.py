Input = open("./(2021)_seventh_edition/data/data2.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(map(str, values.split("\n")))

#Part I
def place(L) :
    """
        input : L is a list of string which is composed of a direction and the length of the move attach to the direction
        output : the needed product between forward and depth 
    """

    forward = 0
    depth = 0
    
    for i in L :
        #check if the input is a "forward" or a "up" and "down"
        if "forward" in i :
            #if forward is the input increase forward
            forward+=int(i[-1])
        else : 
            #if it is not forward increase depth if the input is "down" and decrease it if it is "up" 
            depth+= int(i[-1]) if "down" in i else -int(i[-1])
    
    return forward*depth 


#Part II
def place_aim(L) :
    """
        input : L is a list of string which is composed of a direction and the length of the move attach to the direction
        output : the needed product between forward and depth 
    """
    
    forward = 0
    depth = 0
    aim = 0
    
    for i in L :
        #check if the input is a "forward" or a "up" and "down"
        if "forward" in i :
            #if forward is the input increase forward and increase the depth 
            forward+=int(i[-1])
            depth+=(int(i[-1])*aim)
        else : 
            #if it is not forward increase aim if it is "down" and decrease if it is "up"
            aim+= int(i[-1]) if "down" in i else -int(i[-1])
    
    return forward*depth 

