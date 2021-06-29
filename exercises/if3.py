#compar 2 nombres y verificar si hay coincidencias
#si ambos comienzan con la misma letra o terminan
name1=input("insert name 1: ")
name2=input("insert name 2: ")
if name1==name2:
    print("both names are equal")
elif name1[1]==name2[1]:
    print("the first letter is equal")
elif name1[-1]==name2[-1]:
    print("the last letter is equal")
else:
    print("the names are diferent")
