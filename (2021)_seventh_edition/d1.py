Input = open("./data/2021/data1.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(map(int, values.split('\n')))

#Part I
def incrI(L) :
    res = 0

    #for each member of the list from the second to the last 
    for i in range(1, len(L)) :
        #test is it is greater than the one before 
        if L[i] > L[i-1] : res+=1
    
    return res 


#Part II
def bythree(L) :
    temp = []

    #segmentation of the list with a segment of length 3
    for i in range(len(L)-2) :
        temp.append(L[i]+L[i+1]+L[i+2])

    #apply the precedent function on the new list 
    return incrI(temp)

# print(incrI(list_of_values)) #-> Part I
# print(bythree(list_of_values)) #-> Part II