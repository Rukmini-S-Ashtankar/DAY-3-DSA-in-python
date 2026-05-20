# Row wise max value
# [[100, 198, 333, 323],
# [122, 232, 221, 111],
# [223, 565, 245, 764]]


mylist = [[100, 198, 333, 323],
 [122, 232, 221, 111],
 [223, 565, 245, 764]]

newlist = []
for i in range(3):   #i=0
    j=0
    max = mylist[i][j]  #[0][0]      | max = 333
    for j in range(4):   #j=3
        c_max = mylist[i][j]  #[0][3]   # c_max =323
        if max < c_max:    #333 < 323
            max = c_max
    newlist.append(max)

print(newlist)     


#-------------+++----------------         else this method


    # for row in matrix:
    #     print(max(row))