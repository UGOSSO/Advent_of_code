Input = open("./data/2022/data9.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list([j[0], int(j[1])] for j in (list(map(str, i.split(' '))) for i in list(map(str, values.split('\n')))))

#Work for part I and part II
to_go = {"L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1)}
def update_pos(xhead, xtail, yhead, ytail) :
    xdiff, ydiff = xhead-xtail, yhead-ytail
    possible = {(2,0):(1,0), (-2,0):(-1,0), (0,2):(0,1), (0,-2):(0,-1), (2,1):(1,1), (2,-1):(1,-1), (-2,1):(-1,1), (-2,-1):(-1,-1), (1,2):(1,1), (-1,2):(-1,1), (1,-2):(1,-1), (-1,-2):(-1,-1), (2,2):(1,1), (-2,-2):(-1,-1), (-2,2):(-1,1), (2,-2):(1,-1)}
    return possible[(xdiff, ydiff)]

def nb_tail(L) :
    rope = [[0,0] for i in range(10)]
    visitedI, visitedII = {(0,0)}, {(0,0)}

    for i in L :
        direction, distance = i[0], i[1]
        for i in range(distance) : 
            #increment the head 
            rope[0][0]+=to_go[direction][0]
            rope[0][1]+=to_go[direction][1]

            for i in range(1, len(rope)) :
                #check if the current tail need to move 
                if (abs(rope[i][0]-rope[i-1][0]) > 1) or (abs(rope[i][1]-rope[i-1][1]) > 1) :
                    temp = update_pos(rope[i-1][0], rope[i][0], rope[i-1][1], rope[i][1])
                    rope[i][0]+=temp[0]
                    rope[i][1]+=temp[1]

            #add the current point of tail to the list of visited point index I for part I and -1 for part II
            visitedI.add((rope[1][0],rope[1][1]))
            visitedII.add((rope[-1][0],rope[-1][1]))

    #return the len of the visited point minus the one which appear multiple time 
    return (len(set(visitedI)), len(set(visitedII)))

print(nb_tail(list_of_values)) #index 0 for part I and index 1 for part II