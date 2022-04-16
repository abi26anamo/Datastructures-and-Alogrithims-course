def quickSortLast(lst,first,last):
    
    if first < last:
        pivotIndex = partition(lst,first,last)
        quickSortLast(lst,first,pivotIndex - 1)
        quickSortLast(lst,pivotIndex+1,last)

def partition(lst , first,last):
    pivot = lst[last]
    i =  first+1
    j = last
    while i < j:
         while i < last and lst[i] <=pivot:
             i+=1
         while j > first and lst[j] >= pivot:
             j-=1
         if i < j:
             lst[i],lst[j] = lst[j],lst[i]

    if lst[i] > pivot:
        lst[i],lst[last]  = lst[last],lst[i]
    return i

lst =[345,63,2,63,26,2,2,63]
quickSortLast(lst,0,len(lst)-1)
print(lst)


