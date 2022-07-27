#=====================================================================================================================
#QUICKSORT
#=====================================================================================================================

def quickSort(alist):
	quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
	print("quicksort", alist, first, last)
	if first<last:
		splitpoint = partition(alist,first,last)
		quickSortHelper(alist,first,splitpoint-1)
		quickSortHelper(alist,splitpoint+1,last)
def partition(alist,first,last):
   print("partition", alist, first, last)
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark



def quickSort2(alist):
	quickSortHelper2(alist, 0, len(alist)-1)
def quickSortHelper2(alist, start, end):
	if start < end:
		partition = partition2(alist, start, end)
		quickSortHelper2(alist, start, partition-1)
		quickSortHelper2(alist, partition+1, end)
def partition2(alist, start, end):
	pivot = alist[start]
	left = start + 1
	right = end
	done = False
	while not done:
		if left <= right and alist[left] <= pivot:
			left = left + 1
		if right >= left and alist[right] >= pivot:
			right = right - 1
		if left > right:
			done = True
		else:
			temp = alist[left]
			alist[left] = alist[right]
			alist[right] = temp
	temp = alist[right]
	alist[right] = alist[start]
	alist[start] = temp
	return right 
 
	

alist = [2,4,3,1]
quickSort2(alist)
print("quick: ", alist)