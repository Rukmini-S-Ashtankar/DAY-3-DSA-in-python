name = "Rukmini*is*a*good*programmer"
newname = ''
val = ''
for i in name:
    if i !='*':
        newname += i
    else:
        val+=i                   #can only concatenate str (not "int") to str --appears if mistakenly you put 1 instead og i
print(newname)
print(str(val+newname))