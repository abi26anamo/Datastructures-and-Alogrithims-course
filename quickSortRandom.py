import random
def quickSortRandome(lst,l,r):
    if l >= r:
        return

    p= partiton(lst,l,r)
    quickSortRandome(lst,l,r-1)
    quickSortRandome(lst,l+1,r)
def partiton(lst,l,r):
    p = random.randint(l,r)
    lst[r],lst[p] =lst[p],lst[r]
    for j in range(l,r):
        if lst[j] + lst[r] > lst[l] + lst[j]:
            lst[l],lst[j]= lst[j],lst[l]
            l+=1
            lst[r],lst[l] = lst[l],lst[r]
    return l
     
lst = [4,5,34,34,2,2,56,6]

quickSortRandome(lst,0,len(lst)-1)

print(lst)