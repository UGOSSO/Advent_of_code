Input = open("./data.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(map(str, values.split("\n")))

#complexity will be optimized
#Part I 
#dumb in term of complexity but usable within this range of input size 
def nb_visible(L) :
    res = 0

    for j in range(len(L[0])) :
        for i in range(len(L)) :
            if all(L[i][k] < L[i][j] for k in range(j)) or all(L[i][k] < L[i][j] for k in range(j+1, len(L[i]))) or all(L[k][j] < L[i][j] for k in range(i)) or all(L[k][j] < L[i][j] for k in range(i+1, len(L))) : res+=1

    return res

#two time faster
def nb_visible_bis(L) : 
    lwood = len(L[0])
    hwood = len(L)
    res = 0

    for j in range(lwood) : 
        for i in range(hwood) :
            current = L[i][j]
            l, r, h, b = True, True, True, True 
            
            for k in range(j) :
                if L[i][k] >= current : 
                    l = False 
                    break
            
            for k in range(j+1, lwood) :
                if L[i][k] >= current : 
                    r = False 
                    break

            for k in range(i) :
                if L[k][j] >= current : 
                    h = False 
                    break

            for k in range(i+1, hwood) :
                if L[k][j] >= current :
                    b = False
                    break
            
            if l or r or h or b : res+=1

    return res 

#Part II
def nb_visible_fh(L) :
    res = 0

    for j in range(len(L[0])) :
        for i in range(len(L)) :
            temp1 = 0
            for k in range(j+1) :
                if all(L[i][k] < L[i][j] for k in range(k+1, j)) :
                    if j-k > temp1 : temp1 = j-k
                else : break
                
            temp2 = 0
            for k in range(j, len(L[i])) :
                if all(L[i][k] < L[i][j] for k in range(j+1, k)) :
                    if k-j > temp2 : temp2 = k-j
                else : break

            temp3 = 0
            for k in range(i+1) :
                if all(L[k][j] < L[i][j] for k in range(k+1, i)) :
                    if i-k > temp3 : temp3 = i-k
                else : break

            temp4 = 0
            for k in range(i, len(L)) :
                if all(L[k][j] < L[i][j] for k in range(i+1, k)) :
                    if k-i > temp4 : temp4 = k-i
                else : break
        
            if temp1*temp2*temp3*temp4 >= res : res = temp1*temp2*temp3*temp4

    return res        

# print(nb_visible_bis(list_of_values)) #-> Part I
# print(nb_visible_fh(list_of_values)) #-> Part II