# def the main type of DS that we use to avoid error in the code below
liste = []
string = ''

# create a list of char from a string by spliting at char 
list_of_values = list(map(str, string.split('char')))

# create a list of int from a string by spliting at char 
list_of_values = list(map(str, string.split('char')))

# in a list of string transform the string into a list of string  
list_of_values = list(list(map(str, i.split("char"))) for i in liste)

# in a list of string transform the string into a list of integer  
list_of_values = list(list(map(int, i.split("char"))) for i in liste)

# transform this kind of list [['xchary' , 'wcharz'], ['xchary' , 'wcharz']] into [[[x, y] , [w, z]], [[x, y] , [w, z]]]
list_of_values = list([list(map(int, i[0].split("char"))), list(map(int, i[1].split("char")))] for i in liste)

# generalization of line ten with j string in each list instead of two 
list_of_values = list([list(map(int, j.split("char"))) for j in i] for i in list_of_values)

# transform a list of two integer [x, y] into [x, x+1, x+2, ..., y-2, y-1, y]
list_of_values = list(range(liste[0], liste[1]+1))

# make a DS that can be used as a matrix 
# transform several lines separated by a char of string separated by a char to a list of len(nb_of_lines) composed by list containing the strings of one line splited at char 
list_of_values = list(list(map(str, j.split("char"))) for j in list(i.split("char") for i in liste))

# same as line 28 but with int at the end 
list_of_values = list(list(map(int, j.split("char"))) for j in list(i.split("char") for i in liste))

# replace an unhelpefull char by another char in a string
liste = liste.replace("char", "char")