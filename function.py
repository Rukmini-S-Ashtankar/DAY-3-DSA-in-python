# def hello():      #called funstion
#     print("Hello World")

# hello()    #calling function
# hello()
#                          #prints HEllo World twice


# def arithmetic():
#     a = int(input("Enter the value of a: "))
#     b = int(input("Enter the value of b: "))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul      #if this line is removed then it returns None

# print(arithmetic())           #can be written like - result = arithmetic()
                          #print("Arithmetic =",result)


#------------------------+++------------------
# Positional argument

# def arithmetic(a, b):
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul      #if this line is removed then it returns None
# #positional argument
# result = arithmetic(5,7)          #value should be entered here
# print("Arithmetic =", result)

#-------------------+++----------------------
# Keyword argument

# def credential(username, password):
#     if username == password:
#         print("login successfully")
#     else:
#         print("invalid credentials")
    
# credential(username ="mini", password ="mini")   #calling function

#-------------------+++---------------------
#Default argument

# def cityName(city = "Mumbai"):
#     print(city)

# cityName("Nagpur")             #will call city then print Nagpur same for pune
# cityName("Pune")          #this positional argument will be copied to city parameter #1
# cityName()              #default argument will be printed 

#---------------------+++----------------------
# Variable length argument

# def cityName(*name):
#     print(name)
    
# cityName("Nagpur","Mumbai","Pune","Nashik")

#=============+++================
# Modularity approach