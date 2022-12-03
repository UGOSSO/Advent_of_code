Input = open("./data/2022/data3.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(map(str, values.split('\n')))

#Part I
def in_both_part(L) :
    res = 0

    for i in L :
        for j in i :
            if j in set(i[:len(i)//2]) & set(i[len(i)//2:]) :
                temp = j 
                
  
        if temp in 'azertyuiopqsdfghjklmwxcvbn' : res += ord(temp) - 96
        if temp in "AZERTYUIOPQSDFGHJKLMWXCVBN" : res += ord(temp) - 38

    return res

#Part II
def in_three(L) :
    res = 0

    for i in range(0, len(L)-2, 3) :
        for element in L[i]:
            if element in L[i+1] :
                if element in L[i+2] :
                    temp = element
        
  
        if temp in 'azertyuiopqsdfghjklmwxcvbn' : res += ord(temp) - 96
        if temp in "AZERTYUIOPQSDFGHJKLMWXCVBN" : res += ord(temp) - 38

    return res 


# print(in_both_part(list_of_values)) #-> Part II
# print(in_three(list_of_values)) #-> Part I