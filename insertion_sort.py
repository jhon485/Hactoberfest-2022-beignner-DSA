def insertion_Sort(P):
	for i in range(1, len(P)):
		ans = P[i]
		j = i-1
		while j >=0 and ans < P[j] :
				P[j+1] = P[j]
				j -= 1
		P[j+1] = ans



array = [100,2000,4000,50500,7900]
insertion_Sort(array)
empty_list = []
print("Sorted array is : ")
for i in range(len(array)):
	empty_list.append(array[i])	 
print(empty_list)


