def selection_Sort(input_array, size):
	
	for p in range(size):
		count = p

		for j in range(p + 1, size):
			
			if input_array[j] < input_array[count]:
				count= j
		
		(input_array[p], input_array[ans]) = (input_array[ans], input_array[p])

input_array = [23 ,34,355,-45435,3454,3454,5767,-4,34,-655,747]
size = len(input_array)
selection_Sort(input_array, size)
print('Sorted array:')  # the sorted array in asending order
print(input_array)
