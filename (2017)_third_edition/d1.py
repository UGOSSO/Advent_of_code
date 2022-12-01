Input = open("./data/2017/data1.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
string_of_values = values

#Part I
def capcha(S) : 
    res = 0 

    for i in range(len(S)) :
        #check if the current number is the same than the next number, the modulo is here because the last number need the match the first one 
        if S[i] == S[(i+1)%len(S)] : res+=int(S[i])
    
    return res 

#Part II
def capcha2(S) :
    res = 0 
    temp = len(S)//2

    for i in range(len(S)) :
        #check if the current number is the same than the temp number after, the modulo is here because the last temp number need the match the first temp  
        if S[i] == S[(i+temp)%len(S)] : res+=int(S[i])

    return res 