Input = open("./data/2022/data2.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(map(str, values.split('\n')))

#work for part I and part II
def score2(L) :
    res = 0 
    
    #the key is the input and the values is the one attribuated by the game's rules
    dico_part1 = {'A X':4, 'A Y':8, 'A Z':3, 'B X':1, 'B Y':5, 'B Z':9, 'C X':7, 'C Y':2, 'C Z':6}
    dico_part2 = {'A X':3, 'A Y':4, 'A Z':8, 'B X':1, 'B Y':5, 'B Z':9, 'C X':2, 'C Y':6, 'C Z':7}

    #make a list of the values of each paly and return their sum
    return sum([dico_part1[i] for i in L]), sum([dico_part2[i] for i in L])

