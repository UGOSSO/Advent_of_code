Input = open("data.txt", "r")
values = Input.read()
Input.close()

list_of_values = list(map(str, values.split("\n")))

#Part I
def place(L) :
    forward = 0
    depth = 0
    
    for i in L :
        if "forward" in i :
            forward+=int(i[-1])
        else : 
            depth+= int(i[-1]) if "down" in i else -int(i[-1])
    
    return forward*depth 


#Part II
def place_aim(L) :
    forward = 0
    depth = 0
    aim = 0
    
    for i in L :
        if "forward" in i :
            forward+=int(i[-1])
            depth+=(int(i[-1])*aim)
        else : 
            aim+= int(i[-1]) if "down" in i else -int(i[-1])
    
    return forward*depth 

