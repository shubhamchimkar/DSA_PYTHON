import array

# creating an array
arr = array.array('i',[1,2,3])

#slicing in array
print(arr[0:3]) 

#append in array
arr.append(10)
print(arr) 

#pop in array
arr.pop()
print(arr) 

#pop with index in array
arr.pop(0)

print(arr)
print(arr[0])  

#loop to pop all elements in array
for i in range(0,1):
    arr.pop()
    print(arr)