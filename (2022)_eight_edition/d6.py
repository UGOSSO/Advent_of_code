Input = open("./data.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
string_of_values = values

def lenght4(S) :
    conte = 0

    for j in range(len(S)) :
        #we check begining from the current position the next 4 char are all different if they are all diff 
        #if it is the case we return the position where the start-of-packet marker begin + the number of char in it
        if all(S[j:j+4].count(i) == 1 for i in S[j:j+4]) : return j+4


def lenght14(S) :
    conte = 0

    for j in range(len(S)) :
        #we check begining from the current position the next 14 char are all different if they are all diff 
        #if it is the case we return the position where the start-of-packet marker begin + the number of char in it
        if all(S[j:j+14].count(i) == 1 for i in S[j:j+14]) : return j+14

# print(lenght4(string_of_values)) #-> Part I
# print(lenght14(string_of_values)) #-> Part II