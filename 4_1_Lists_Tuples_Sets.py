cources = ['History', 'Math', 'Physics', 'CompSci']
print(cources)

#length
print(len(cources))

#first item
print(cources[0])

#third item
print(cources[3])

#last item
print(cources[-1])

#slicing
print(cources[0:2])

print(cources[:2])

print(cources[2:])

#append
cources.append('Art')
print(cources)

#insert
cources.insert(0, 'Art')
print(cources)

#extend
cources = ['History', 'Math', 'Physics', 'CompSci']
cources_2 = ['Education', 'Chemistry']
cources.insert(0, cources_2)
print(cources)

cources = ['History', 'Math', 'Physics', 'CompSci']
cources_2 = ['Education', 'Chemistry']
cources.extend(cources_2)
print(cources)

#remove
cources.remove('Math')
print(cources)

#pop
popped = cources.pop()
print(popped)
print(cources)

#reverse
cources.reverse()
print(cources)

#sort
cources.sort()
print(cources)

#sort
cources.sort(reverse=True)
print(cources)

#sort
cources = ['History', 'Math', 'Physics', 'CompSci']
sorted_cources = sorted(cources)   
print(sorted_cources)

#sort
nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)

#sort
nums = [1, 5, 2, 4, 3]
sorted_nums = sorted(nums)
print(sorted_nums)

#sort
nums = [1, 5, 2, 4, 3]
print(min(nums))
print(max(nums))
print(sum(nums))

#sort
cources = ['History', 'Math', 'Physics', 'CompSci']
print(cources.index('CompSci'))
print('Art' in cources)
print('Math' in cources)

#sort
for item in cources:
    print(item)

#sort
for index, item in enumerate(cources):
    print(index, item)

#sort
for index, item in enumerate(cources, start=1):
    print(index, item)

#sort
cources_str = ', '.join(cources)
print(cources_str)

#sort
new_list = cources_str.split(', ')