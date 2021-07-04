one = 'first string with single quotes'
print(one)
two = "second string with doble quotes"
print(two)
three = 'doesn\'t'#we use \' to scape the single quote
print(three)
four = "doesn't"# we can use doble quotes to include single quote
print(four)
five = "\"yes\", they said"# we can use \" too"
print(five)
six = "First line\nSecond line"# we use \n to include a new line
print(six)
#seven = "C:\user\name"
# this will include a new line, and will create an error
#C:\user
#ame
# to avoid this we will use: 'print (r"C:\user\name")' or
# seven= "C:/user/name"
print(r"C:\user\name")
eigth = """usuario : gary [OPTIONS]
    -h          Display this usage message
    -H          hostname to connect"""# we can use parragraph too
print(eigth)
nine = "Python"
print(nine[2]) # print the second character
print(nine[-2]) # print the second-last character
print(nine[0:2]) # print characters from 0 to 2 [0;2)
print(nine[:3])
print(len(nine)) # print the length of a string
