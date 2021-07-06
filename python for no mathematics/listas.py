# introduction to list
arr = ["futbol","basket",18,True,[False,14.4]]
print(arr)
# print just one value
print(arr[2])
# print last value
print(arr[-1])
# print values from 0 to 2 [0;2)
print(arr[0:2])
# array size
print(len(arr))
# insert new value
arr.append(43)
# insert new value with index
arr.insert(1,88)
# insert an array of values
arr.extend([True,"char","hi"])
# join of arrays
arr2=["second array","good bye",19.3,19.3,19.3]
arr3=arr+arr2
# serch in array returns a boolean
print("futbol" in arr)
# serch the index in array
print(arr.index("futbol"))
# count values in array
print(arr2.count(19.3))
# remove a value in array
print(arr.remove("futbol"))
# clean an array
arr.clear()
# reverse an array
arr2.reverse()
# sort an array asc
arr4=[1,4,5,6.3,-1,34,-9]
arr4.sort()
#sort an array desc
arr4.sort(reverse=True)
print(arr4)
