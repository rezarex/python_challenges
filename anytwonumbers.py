#function definition
'''
return true if any two numbers in list add up to the provided k
'''

def anyTwoNumbers(lst, k):
    #create set to avoid case where a number is double itself
    lst_set = set(lst)

    return any(k-i in lst_set for i in lst_set)
   




#driver code
lst = [10, 15, 3, 7]
k = 20
print(anyTwoNumbers(lst, k))