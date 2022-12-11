Input = open("./data/2022/data11.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
import re 
import math 

list_of_values = list(map(str, values.split('\n\n')))
list_of_values = [i.split('\n') for i in list_of_values]
list_of_values = [list(j.replace('  ', '').replace('    ', '') if j[0] == ' ' else j for j in i) for i in list_of_values]
op = [j[2][21] for j in list_of_values] 
list_of_values = [list(list(int(d) for d in re.findall(r'\b\d+\b', j)) for j in i) for i in list_of_values]

elt = [i[1] for i in list_of_values]
mult = [i[2][0] if i[2] != [] else -1 for i in list_of_values]
div = [i[3][0] for i in list_of_values]
throw_to = [[i[-2][0], i[-1][0]] for i in list_of_values]
func = [0] * len(op)

#take the lcm of the div for the part II
from math import lcm

maxn = math.lcm(*[i for i in div])

#make a list with the function for use at each round 
def makefx(x) :
    return lambda k: k * x
def makefp(x) :
    return lambda k: k + x
for i in range(len(op)) :
    if mult[i] == -1 :
        func[i] = (lambda x: x * x) if "*" == op[i] else (lambda x: x + x)
    else : 
        func[i] = makefx(mult[i]) if "*" == op[i] else makefp(mult[i])

#work for both part I and II
import copy

def partIbis(elt, round, partII = False) :
    #make a deepcopy of elt to be able to call the function multiple time
    helt = copy.deepcopy(elt)
    #the number of inspection for each monkey
    restemp = [0] * len(elt)

    for i in range(round) :
        for j in range(len(elt)) :
            for k in helt[j] :
                #increase the inspection
                restemp[j]+=1

                #change the value of k according to the part
                k = func[j](k)
                k = k % maxn if partII else k // 3 

                #throw the object to the other monkey 
                helt[throw_to[j][0] if k % div[j] == 0 else throw_to[j][1]].append(k)

            #after id round the monkey is clear of all is elt 
            helt[j] = []
    
    #to find the business lvl we sort the list of inspection and multiply the two greatest elt
    restemp = sorted(restemp)

    return restemp[-1] * restemp[-2]

# print(partIbis(elt, 20), partIbis(elt, 10000, True)) #-> first call for part I second part II