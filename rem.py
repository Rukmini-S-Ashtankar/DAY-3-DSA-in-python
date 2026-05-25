#Remove spaces from string:
# 1. rstrip()===> To remove spaces at right hand side
# 2. lstrip()===> To remove spaces at the left side
# 3. strip()===> To remove spaces from both sides

city=input("Enter the city Name: ")
scity=city.strip()
print(scity)