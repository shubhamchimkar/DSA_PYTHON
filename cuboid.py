#This program is to generate a list of all possible coordinates in a cube which are not equal to n
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
z = int(input("Enter the value of z: "))
n = int(input("Enter the value of n: "))

#empty list to store the coordinates
final_list=[]
#loop to generate all coordinates
for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            #if the sum of the coordinates is not equal to n, then append to the list
            if a+b+c != n:
                final_list.append([a,b,c])
#Print the list of coordinates
print(final_list)

#Using list comprehension to generate the same list
final_list_comp=[[a,b,c] for a in range (x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]

#Print the list of coordinates using list comprehension
print(final_list_comp)