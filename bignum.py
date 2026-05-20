# Find the biggest number
def findBiggestNumber(sampleArray):          #[5,7,9,2,3,4]
    biggestNumber = sampleArray[0]            #biggestNumber = 5 #filhal till searched further  #===========>O(1)
    for index in range(1,len(sampleArray)):     #index = 1                          #=========> O(N)
        if sampleArray[index] > biggestNumber:    #7 > 5                            #===========>O(1)
            biggestNumber = sampleArray[index]                                      #===========>O(1)
    print(biggestNumber)                                                            #===========>O(1)

sampleArray = [5,7,9,2,3,4]
findBiggestNumber(sampleArray)             # o/p 9

# O(1) + O(1) + O(1) + O(1) + O(N) = O(N)

# -----------   Ask ChatGPT to expplain time complexity line by line
# ----------- When you prepare for higher end, lower end can be prepared automatically