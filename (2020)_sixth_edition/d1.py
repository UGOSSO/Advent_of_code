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
            return i*(2020-i)

#Part II
def expense_report_3(L) :
    """
        input : L is a list of integer 
        output : the product between the three number in L which sum egal to 2020
    """
    
    for i in range(len(L)):
        for j in range(len(L)):
            if i!=j:
                if 2020-L[i]-L[j] in L :
                    ind = [ind for ind, x in enumerate(L) if x == 2020-L[i]-L[j]]
                    
                    if i in ind : lim = 1
                    else : lim = 0
                    
                    if j in ind : lim += 1
                    
                    if len(ind)> lim:
                        print( (2020-L[i]-L[j])*L[i]*L[j])

# print(expense_report_2(list_of_values)) #-> Part I
# print(expense_report_3(list_of_values)) #-> Part II