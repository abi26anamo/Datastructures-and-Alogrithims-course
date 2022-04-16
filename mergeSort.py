
def mergeSort(lst):
    if len(lst)>1:
         firsthalf = lst [: len(lst)//2]
         secondhalf = lst[len(lst)//2:]
         mergeSort(firsthalf)
         mergeSort(secondhalf)
         merge(firsthalf,secondhalf,lst)

def merge(lst1,lst2,lstSorted):
    i=0;
    j=0;
    k=0;

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            lstSorted[k] = lst1[i]
            i+=1
            k+=1
        else:
            lstSorted[k] = lst2[j]
            j+=1
            k+=1
    while i < len(lst1):
            lstSorted[k] = lst1[i]
            i+=1
            k+=1
    while j < len(lst2):
                lstSorted[k] = lst2[j]
                j+=1
                k+=1
def main():
    lst = [23,3,45,7,3,45,2,3]
    print('list before sorting ')
    print(lst)
    mergeSort(lst)
    print('list after sorting')
    print(lst)
main()