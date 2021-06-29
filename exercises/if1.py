#2 numeros y cual es par
a = int(input("insert number 1:"))
b = int(input("insert number 2:"))
if a%2==0 and b%2==0:
    print("the two numbers are pair")
elif a%2==0:
    print("the number 1 is pair")
elif b%2==0:
    print("the number 2 is pair")
else:
    print("no number is pair")
