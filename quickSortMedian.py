def swap(lst,a,b):
    lst[a],lst[b] = lst[b],lst[a]
def partition(lst,first,last):
    median = (last - 1 - first) // 2
    median = median + first
    left = first + 1
    if (lst[median] - lst[last-1])*(lst[first]-lst[median]) >= 0:
        swap(lst,first,median)
    elif (lst[last - 1] - lst[median]) * (lst[first] - lst[last - 1]) >=0:
         swap(lst,first,last - 1)
    pivot = lst[first]
    for right in range(first,last):
        if pivot > lst[right]:
            swap(lst,left,right)
            left = left + 1
    swap(lst,first,left-1)
    return left-1
def quickSortHelper(lst,first,last):
    if first < last:
        pivotindex = partition(lst,first,last)
        quickSortHelper(lst,first,pivotindex)
        quickSortHelper(lst,pivotindex+1,last)
def quickSort(lst):
    quickSortHelper(lst,0,len(lst))
lst = [66,45,65,66,23,65,3422,213,56]
quickSort(lst)
print(lst)



