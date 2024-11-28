dict={}

dict=()

my_dict= {
    "name":"shubham",
    "city":"Vasai",
    "role":"Devops"
}

print(my_dict["role"])
print(my_dict.get("role"))

my_dict["salary"]= 1000

print(my_dict)

my_dict.update({"role":"engineer"})
my_dict.update({"hobby":"music"})
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

for key,value in my_dict.items():
    print(key,value)