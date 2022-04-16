def quickSortMiddle(lst,first,last):
    
    if first < last:
        pivotIndex = partition(lst,first,last)
        quickSortMiddle(lst,first,pivotIndex)
        quickSortMiddle(lst,pivotIndex+1,last)

def partition(lst,first,last):
    i= first-1
    j= last+1
    pivot = lst[(first + last)//2]
    

    while True:
        i+=1
        while lst[i] < pivot:
            i+=1
        
        j-=1
        while lst[j] > pivot:
            j-=1
        if i >=j:
             return j
        lst[i],lst[j]= lst[j],lst[i]
   

lst =[23,5,23,634,1,54,1,2]
quickSortMiddle(lst,0,len(lst)-1)

print(lst)

