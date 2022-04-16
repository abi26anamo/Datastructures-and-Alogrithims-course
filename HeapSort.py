from heap import Heap

def Heapsort():
    heap = Heap()

    for v in lst:
        heap.add(v)

    for i in range(len(lst)):
        list[len(list)-1-v] = heap.remove

def main():
    lst = [5,-3,6,3,-4,9]
    Heapsort(lst)
    for v in lst:
        print(str(v) + " ", end ="")
    
  # if r < len(self.__lst):
            #     if self.__lst[r] > self.__lst[maxindex]:
            #         maxindex = r


            # if self.__lst[i] < self.__lst[maxindex]:
            #     self.__lst[maxindex],self.__lst[i] = self.__lst[i], self.__lst[maxindex]
            #     i = maxindex
            # else:
            #     break