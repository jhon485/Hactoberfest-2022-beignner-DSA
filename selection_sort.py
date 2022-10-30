def selectionSort(brr, size):
	
	for p in range(size):
		ans = p

		for j in range(p + 1, size):
			
			if brr[j] < brr[ans]:
				ans= j
		
		(brr[p], brr[p]) = (brr[ans], brr[ans])

array = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(array)
selectionSort(array, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(array)
