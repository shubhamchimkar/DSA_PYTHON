import timeit
#check which one is faster
#list
print(timeit.timeit('x=[1,2,3,4]', number=1000000))
#tuple
print(timeit.timeit('x=(1,2,3,4)', number=1000000))

