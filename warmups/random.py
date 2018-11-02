import random
#list compression
arr = [x for x in range(100)]
rand_arr = [random.randint(0,100) for x in range(10)]
print(rand_arr)
#access array 
print(arr[50])
print(arr[len(arr)//2])
print(arr[-1])
