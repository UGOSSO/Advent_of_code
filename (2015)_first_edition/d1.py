Input = open("./(2015)_seventh_edition/data1.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
string_of_values = values

#Part I
def floor(S) :
    #substract the number of "(" and the number of ")"
    return S.count("(")-S.count(")")

#Part II
def basement(S) :
    floor = 0 

    for i in range(len(S)) :
        #check the next floor 
        if S[i] == "(" : floor+=1
        if S[i] == ")" : floor-=1

        #if we arrived in the basement return the index of the ")"
        if floor == -1 : return i+1
    
    return False