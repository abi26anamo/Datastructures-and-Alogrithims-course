class Heap():
    def __init__(self):
        self.Nodes = []

    def add(self,num):
        self.Nodes.append(num)
        i = len(self.Nodes)-1
        while i > 0:
            parentindex = (i -1)//2
            if self.Nodes[i] > self.Nodes[parentindex]:
                self.Nodes[i],self.Nodes[parentindex] = self.Nodes[parentindex],self.Nodes[i]
            else:
                break
            i = parentindex

    def remove(self):
        if len(self.Nodes) == 0:
            return None
        popped = self.Nodes[0]
        self.Nodes[0] = self.Nodes[len(self.Nodes)-1]
        self.Nodes.pop(len(self.Nodes)-1)

        i = 0
        while i <  len(self.Nodes):
            l = i * 2 + 1
            r = i * 2 + 2
            if l > len(self.Nodes)-1:
                break
            if r > len(self.Nodes)-1:
                break
            maxindex = l if self.Nodes[r]< self.Nodes[l] else r

            if self.Nodes[r] > self.Nodes[maxindex]:
                self.Nodes[r],self.Nodes[maxindex] = self.Nodes[r], self.Nodes[maxindex]
            if self.Nodes[l] > self.Nodes[maxindex]:
                self.Nodes[l],self.Nodes[maxindex] = self.Nodes[l], self.Nodes[maxindex]
            i+=1
           

        return popped
    def getSize(self):
        return len(self.Nodes)
    def isEmpty(self):
        return len(self.Nodes) == 0
    def peek(self):
        return self.Nodes[0]

def main():
    myHeap = Heap()

    listToSort = [9,2,7,11]
    for i in range(len(listToSort)):
        myHeap.add(listToSort)
    for i in range(len(listToSort)):
         myHeap.remove()
    print(listToSort)
   

    
main()

