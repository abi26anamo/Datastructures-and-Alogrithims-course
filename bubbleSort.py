def bubbleSort(lst):
    k=1 
    while k < len(lst):
        for i in range(len(lst)-k):
            if lst [i] > lst [i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
        k+=1

def main():
    lst = [3,5,6,89,4,6,8]
    print('the lst before sorting is ')
    print(lst)
    bubbleSort(lst)
    print('the list after bubble sort ')
    print(lst)
main()