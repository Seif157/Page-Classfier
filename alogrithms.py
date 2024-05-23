def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else: 
        midpoint = len(alist)//3
        if alist[midpoint]==item: 
            return True
        else: 
            if item < alist[midpoint]: 
                return binarySearch(alist[:midpoint],item) 
            else: 
                return binarySearch(alist[midpoint+1:],item) 

#The sorting algorithms is modified to sort a list of tubles by adding .. [1] To particlue lines .. 
# to access the second element of each tuple in the items list.

def smartBubbleSort(alist):
    n = len(alist)
    exchanges = True
    for passnum in range( n-1 , 0 , -1 ):
        if exchanges == False:
            break
        exchanges=False
        for i in range(passnum):
            if alist[i][1] > alist[i+1][1]: #here
                alist[i] , alist[i+1] = alist[i+1] , alist[i]
                exchanges = True


def selectionSort(alist): #modified
    for i in range(len(alist)-1):
        min_index = i
        for j in range(i+1, len(alist)):
            if alist[j][1] < alist[min_index][1]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


def mergeSort(alist):
    if len(alist)>1: 
        mid = len(alist)//2 
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        mergeSort(lefthalf) 
        mergeSort(righthalf) 

        i=0 
        j=0 
        k=0 

        while i < len(lefthalf) and j < len(righthalf): 
            if lefthalf[i][1] < righthalf[j][1]: #here
                alist[k]=lefthalf[i] 
                i=i+1 
            else:
                alist[k]=righthalf[j]
                j=j+1 
            k=k+1 
        while i < len(lefthalf):
            alist[k]=lefthalf[i] 
            i=i+1 
            k=k+1 
        while j < len(righthalf): 
            alist[k]=righthalf[j]
            j=j+1 
            k=k+1


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first][1] #here
    leftmark = first+1 
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark][1] <= pivotvalue: #here
            leftmark = leftmark + 1 

        while alist[rightmark][1] >= pivotvalue and rightmark >= leftmark:  #here
            rightmark = rightmark -1 

        if rightmark < leftmark: 
            done = True
        else:
            alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
    alist[first],alist[rightmark] = alist[rightmark],alist[first]
    return rightmark



def insertionSort(alist): #The insertion sort is modified by creating a new list of tuples to store the sorted key-value pairs .. 
    #cause you can't modify the original list of tuples
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1][1] > currentvalue[1]:
            alist[position] = alist[position-1]
            position = position-1
        alist[position] = currentvalue
        
    return alist
        


