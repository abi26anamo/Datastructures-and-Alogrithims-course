

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j= i-1
        for k in range(i):
            if arr[i]<arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                i-=1
                j-=1
def main():
    arr =[23,43,33,132,54,123,54,123]
    insertion_sort(arr)
    print(arr)
main()

