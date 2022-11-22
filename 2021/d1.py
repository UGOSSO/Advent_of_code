Input = open("data.txt", "r")
values = Input.read()
Input.close()

list_of_values = list(map(int, values.split('\n')))

#Part I
def incrI(L) :
    res = 0
    for i in range(1, len(L)) :
        if L[i] >= L[i-1] : res+=1
    
    return res 


#Part II marche pas 
def bythree(L) :
    temp = []
    while L :
        temp.append(sum(L[0 : 3]))
        L[0 : 3] = []
    
    return(temp)
print(len(list_of_values), 2000//3, list_of_values[-1])
print(len(bythree(list_of_values)))
