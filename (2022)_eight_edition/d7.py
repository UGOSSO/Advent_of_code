Input = open("./data.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(map(str, values.split('\n')))
list_of_values = [i for i in list_of_values if 'cd ' in i or any(char.isdigit() for char in i)]
list_of_values = [i.replace('$ ', '') for i in list_of_values]
list_of_values = [list(map(str, i.split(' ')))for i in list_of_values]
#creating a tree
from anytree import Node, RenderTree

nodes = []
home = Node('/')
nodes.append(home)

current = home

for i in list_of_values[1:] : 
    if 'cd' in i :
        if '..' in i :
            current = current.parent 
        else : 
            globals()[i[1]] = Node(i[1], parent=current)
            nodes.append(globals()[i[1]])
            current = globals()[i[1]]
    
    else :
        globals()[i[0]] = Node(i[0], parent=current)
        nodes.append(globals()[i[0]])

#creating a dictionnary with every file size 
fsize = {}
for i in nodes : 
    if any(char.isdigit() for char in i.name) :
        if i.name not in fsize :
            fsize[i.name] = int(i.name)   

#create a memorize func to implement dynamic programing 
def memorize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache: return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func

# creating a size function
def sized(node) :
    if node.name in fsize : return fsize[node.name]
    else : return sum([size(i) for i in node.children])

size = memorize(sized)

#Part I
def partI(tree) :
    res = 0
    
    #add all the dir of less than 100000 data unit
    for i in tree :
        if not i.name.isdigit() and size(i) < 100000 : res+=size(i)

    return res

#Part II
def partII(tree) :
    #find the value that we need to erase
    to_del = sum(fsize.values()) - 40000000

    #check for eaxch dir if it has the smallest value needed to erase all excess data
    size_d = 70000000
    for i in tree :
        if not i.name.isdigit() : 
            temp = size(i) 
            if temp >= to_del and temp < size_d : size_d = temp

    return size_d

# print(partI(nodes)) #-> Part I
# print(partII(nodes)) #-> Part II