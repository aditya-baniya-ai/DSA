nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

frequency = {}

for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
highest = max(frequency, key= lambda x: frequency[x])
print(highest)

#for key,value in frequency.items():
 #   print (key, value)