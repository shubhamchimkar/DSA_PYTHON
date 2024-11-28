import array

arr = array.array('i',[1,2,3])

print(arr[0:3]) #slice
arr.append(10)
print(arr) 
arr.pop()
print(arr) 
arr.pop(0)

print(arr)
print(arr[0])  

for i in range(0,1):
    arr.pop()
    print(arr)