Input = open("./data/2020/data3.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(map(str, values.split("\n")))

#Part I 
def slide(L) :
    res = 0 
    start = 0

    #the loop is making us go down the hill
    for i in range(0, len(L)) :
        #we expand the list because the pattern is repeating but not to much use to much storage  
        L[i]*=((len(L)%len(L[i]))*3)
        
        #test if we arrive on a tree 
        if L[i][start] == "#" : res+=1
        
        #we go three to the right 
        start+=3
        
    return res 

#Part II
def slide_(L) :
    res11, res31, res51, res71, res12, start11, start31, start51, start71, start12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 

    #here we have to loop one that go down one by one and the other two by two for the last test 
    #we do each test in two loop instead of calling the preceding function with other parameters 5 times for increase the time complexity 
    #the loop is making us go down the hill
    for i in range(0, len(L)) :
        #we expand the list because the pattern is repeating but not to much use to much storage 
        L[i]*=((len(L)%len(L[i]))*7)
        
        #test if we arrive on a tree
        if L[i][start11] == "#" : res11+=1
        if L[i][start31] == "#" : res31+=1
        if L[i][start51] == "#" : res51+=1
        if L[i][start71] == "#" : res71+=1
        
        #we go to the right
        start11+=1
        start31+=3
        start51+=5
        start71+=7
        
    #the loop is making us go down the hill
    for i in range(0, len(L), 2) :
        #we expand the list because the pattern is repeating but not to much use to much storage 
        L[i]*=(len(L)%len(L[i]))    
        
        #test if we arrive on a tree
        if L[i][start12] == "#" : res12+=1
        
        #we go to the right
        start12+=1
        
    #return the product of each result of the given slide 
    return  res11*res31*res51*res71*res12

# print(slide(list_of_values)) #-> Part I
# print(slide_(list_of_values)) #-> Part II