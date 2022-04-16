def QS(listToSort):
    if len(listToSort)<=1:
        return listToSort
    else:
        pivot = listToSort.pop()
        leftpart =[]
        rightpart = []
        for x in listToSort:
            if x < pivot:
                leftpart.append(x)
            else:
                rightpart.append(x)
        return QS(leftpart)+[pivot]+QS(rightpart)

def main():
    listToSort = [23,34,634,2,1,23,234,1]
    print('print the list before sorting ')
    print(listToSort)
    QS(listToSort)
    print('the list after sorting is ')
    print(listToSort)

main()