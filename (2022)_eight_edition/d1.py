Input = open("data.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(list(sum(map(int, j)) for j in list(i.split("\n") for i in list(map(str, values.split("\n\n"))))))

#Part I
def most(L) :
    return max(L)

#Part II
def podium(L) :
    return sum(sorted(L)[-3:])