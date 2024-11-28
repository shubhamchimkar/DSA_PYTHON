import timeit
print(timeit.timeit('x=[1,2,3,4]', number=1000000))

print(timeit.timeit('x=(1,2,3,4)', number=1000000))

