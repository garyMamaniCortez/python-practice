balance=2000
'''
1 ingreso dinero
2 retirar dinero
3 mostrar dinero
4 salir
'''
function=int(input("insert a numer from 1 to 4"))
if function==1:
    residue = int(input("insert your new money: "))
    balance = balance+residue
    print(f"your balance is {balance}")
elif function==2:
    residue = int(input("insert the amount: "))
    if balance-residue>=0:
        print(residue)
    else:
        print(f"your balance is lower than the amount")
elif function==3:
    print(balance)
elif function==4:
    print("thank for using our system")
else:
    print("no function available")
