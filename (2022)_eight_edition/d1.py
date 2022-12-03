Input = open("./data/2022/data1.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
#here we make a list of the amount of calories carried for each elf
list_of_values = list(list(sum(map(int, j)) for j in list(i.split("\n") for i in list(map(str, values.split("\n\n"))))))

#Part I
def most(L) :
    return max(L)

#Part II
def podium(L) :
    #return the sum of the last three element of the sorted list 
    return sum(sorted(L)[-3:])

# print(most(list_of_values)) #-> Part I
# print(podium(list_of_values)) #-> Part II