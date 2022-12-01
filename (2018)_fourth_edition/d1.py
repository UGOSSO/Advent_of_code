Input = open("data.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = [int(i) if i[0]=="-" else int(i) for i in list(map(str, values.split('\n')))]

#Part I
def freq(L) :
    return sum(L)

#Part II
def twice(L) :
    #here obtained is a set because it is much more efficient than list for the 'in' test line 23
    obtained = {0}
    freq = 0
    
    #make a loop until we return something, meaning we can browse the list multiple time 
    while True :
        for f in L : 
            #we had the next elt of the list to the freq and if we already obtained it we return it else we add it in the set 
            freq+=f
            if freq in obtained : return freq
            obtained.add(freq)