# Empty dictionary
dict={}

# Empty tuple
dict=()

# Non-empty dictionary
my_dict= {
    "name":"shubham",
    "city":"Vasai",
    "role":"Devops"
}

# Accessing values using key
print(my_dict["role"])
print(my_dict.get("role"))

# Adding new key-value pair
my_dict["salary"]= 1000

# Printing the dictionary
print(my_dict)

# Updating multiple key-value pairs
my_dict.update({"role":"engineer"})
my_dict.update({"hobby":"music"})
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# Iterating over the dictionary
for key,value in my_dict.items():
    print(key,value)