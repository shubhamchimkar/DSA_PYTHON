x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
z = int(input("Enter the value of z: "))
n = int(input("Enter the value of n: "))

final_list=[]
for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if a+b+c != n:
                final_list.append([a,b,c])
print(final_list)

final_list_comp=[[a,b,c] for a in range (x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]

print(final_list_comp)