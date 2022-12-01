Input = open("./data/2016/data2.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(map(str, values.split("\n")))

#Part I
def bathroom_code(L) :
    #array of the digicode arranged by line
    digicode = ["123","456","789"]
    #index of the button in the digicode array init at button 5
    start =  [1, 1]
    code = ''

    for i in L :
        for j in i :
            #go in the given direction
            if j == "L" : start[1]-=1
            elif j == "R" : start[1]+=1
            elif j == "U" : start[0]-=1
            elif j == "D" : start[0]+=1
            
            #check if we are outside of the digicode if we are return in the nearest position 
            if start[0] == -1 : start[0] = 0
            if start[1] == -1 : start[1] = 0
            if start[0] == 3 : start[0] = 2
            if start[1] == 3 : start[1] = 2

        #add each number to the code     
        code+=digicode[start[0]][start[1]]

    return code 

#Part II
def bathroom_code_correct(L) :
    #array of the digicode arranged by column
    digicode = ["5","26A","137BD","48C","9"]
    #index of the button in the digicode array init at button 5
    start = [0, 0]
    code = ''

    for i in L :
        for j in i :
            #for each row check if we can go to the given direction and if we can go go
            if start[0] == 0 : 
                if j == "R" : 
                    start[0]+=1
                    start[1]+=1
                else : pass
            elif start[0] == 1 : 
                if j == "L" and start[1] == 1 : 
                    start[0]-=1
                    start[1]-=1
                if j == "R" : 
                    start[0]+=1
                    start[1]+=1
                if j == "U" and (start[1] == 1 or start[1] == 2) : start[1]-=1
                if j == "D" and (start[1] == 0 or start[1] == 1) : start[1]+=1
            elif start[0] == 2 : 
                if (j == "R" or j == "L") and (start[1] == 1 or start[1] == 2 or start[1] == 3) : 
                    start[0]+=1 if j == "R" else -1
                    start[1]-=1
                if j == "U" and (start[1] == 1 or start[1] == 2 or start[1] == 3 or start[1] == 4) : start[1]-=1
                if j == "D" and (start[1] == 0 or start[1] == 1 or start[1] == 2 or start[1] == 3) : start[1]+=1
            elif start[0] == 3 : 
                if j == "R" and start[1] == 1 : 
                    start[0]+=1
                    start[1]-=1
                if j == "L" : 
                    start[0]-=1
                    start[1]+=1
                if j == "U" and (start[1] == 1 or start[1] == 2) : start[1]-=1
                if j == "D" and (start[1] == 0 or start[1] == 1) : start[1]+=1
            elif start[0] == 4 : 
                if j == "L" : 
                    start[0]-=1
                    start[1]+=1
                else : pass

        #add each number to the code
        code+=digicode[start[0]][start[1]]

    return code