Input = open("./data/2020/data1.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = list(map(int, values.split('\n')))

#Part I
def expense_report_2(L) :
    """
        input : L is a list of integer 
        output : the product between the two number in L which sum egal to 2020
    """

    for i in L :
        #2020-i is in L we have i in L, j = 2020-i in L and i+j = 2020 by definition so we have our two number 
        if 2020-i in L : 
            #check if don't use i two times 
            if L.index(i) != L.index(2020-i) :     
                return i*(2020-i)

#Part II
def expense_report_3(L) :
    """
        input : L is a list of integer 
        output : the product between the three number in L which sum egal to 2020
    """
    
    for i in L :
        for j in L :
            #2020-i-j is in L we have i in L, j in L, k = 2020-i-j in L and i+j+k = 2020 by definition so we have our three number 
            if 2020-i-j in L :
                #check if don't use i or j two times
                if L.index(i) != L.index(2020-i-j) and L.index(j) != L.index(2020-i-j) : 
                    return i*j*(2020-i-j)

# print(expense_report_2(list_of_values)) #-> Part I
# print(expense_report_3(list_of_values)) #-> Part II