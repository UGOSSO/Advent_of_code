Input = open("./data/2022/data5.txt", "r")
stack = ''
for i in range(8) :    
    stack+=Input.readline()
Input.readline()
Input.readline()
values = Input.read()
Input.close()

#transform the input in a usable data structure
#for the stack
stack = list(map(str, stack.split("\n")))
stack = [i.replace("    ", '[0]').replace(' ', '').replace('[', '').replace(']', '') for i in stack[:-1]]
list_of_stack = ['' for i in range(len(stack[0]))]
list_of_stack = ["".join([list_of_stack[i]+j[i] for j in stack]) for i in range(len(stack[0]))]
list_of_stack = [i[::-1].replace('0', '') for i in list_of_stack]
#for the deplacement lines 
list_of_values = list(map(str, values.split("\n")))
list_of_values = list(list(map(str, i.split(' '))) for i in list_of_values)
list_of_values = [[int(i[1]), int(i[3]), int(i[-1])] for i in list_of_values]

#Part I
def crane9000(L, lstack) :
    res = ''
    stack = lstack.copy()

    for i in L :
        #we add the 'move' moved elt of the 'from' stack to the 'to' stack in reverse order 
        stack[i[-1]-1]+=stack[i[1]-1][-i[0]:][::-1]
        #we get rid of them in the stack 'from'
        stack[i[1]-1]=stack[i[1]-1][:-i[0]]

    #get the last elt from each stack
    for i in stack :
        res+=i[-1]

    return res 

#Part II
def crane9001(L, lstack) :
    res = ''
    stack = lstack.copy()

    for i in L :
        #we add the 'move' moved elt of the 'from' stack to the 'to' stack in reverse order 
        stack[i[-1]-1]+=stack[i[1]-1][-i[0]:]
        #we get rid of them in the stack 'from'
        stack[i[1]-1]=stack[i[1]-1][:-i[0]]

    #get the last elt from each stack
    for i in stack :
        res+=i[-1]

    return res 

# print(crane9000(list_of_values, list_of_stack)) #-> Part I
# print(crane9001(list_of_values, list_of_stack)) #-> Part II