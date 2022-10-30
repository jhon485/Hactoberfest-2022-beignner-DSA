def insertion_Sort(array):
	for i in range(1, len(array)):

		key = array[i]
		j = i-1
		while j >=0 and key < array[j] :
				array[j+1] = array[j]
				j -= 1
		array[j+1] = key



array = [1343,3434,53,34345,3243,800]
insertion_Sort(array)
list = [] 
print(" The out is this Sorted array : ")
for i in range(len(array)):
	list.append(array[i])	 
print(list)
