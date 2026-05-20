def linearSearch(array, target):
    for i in range(0, len(array)): #i=0  0 is position(less than 7(size of array), condition True)
        if array[i] == target:    #1 ==7 false (will iterate again)
            return i
    
array = [1,2,3,4,8,7,9]
target = 7    #search the target value i.e 7
linearSearch(array, target)

#then i = 1 (less than 7, True) till index number 6
# 2 == 7 False

# i = 2
# 3 ==7

#i = 3
#4 == 7

#i = 4
# 8 ==7

# i = 5
# 7 == 7 (Condition True, loop end)
