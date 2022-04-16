class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self) :
        self.head = None
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    def addFirst(self,data):
        if self.head is None:
             node = Node(data)
             self.head = node 
        else:
            current = self.head 
            node = Node(data)
            self.head = node 
            self.head.next = current
       
    def removeFirst(self):
        if self.head is None:
            return None
        else:
            current = self.head 
            self.head = current.next
            return current.data
    def addLast(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else :
            current = self.head
            while current.next !=None:
                current = current.next
            node = Node(data)
            current.next = node
    def removeLast(self):
        if self.head is None:
            return None
        else:
            current= self.head
            while current.next !=None:
                current = current.next
            current = None
    def add(self,index,data):
        if index <0 or index >= self.get_length():
            return None
        elif index == 0:
            return self.addFirst()
        
        elif index == 1:
            current = self.head
            node = Node(data)
            current.next = node
            return current.data
        else:
            prev= self.head
            for i in range(1,index):
                prev = prev.next
            temp = prev.next
            node = Node(data)
            prev.next = node
            node.next = temp
    def remove(self,index):
        if index < 0 or index >= self.get_length():
            return None
        if index == 0:
            return self.removeFirst()
        else:
            prev = self.head 
            for i in range(1,index):
                prev = prev.next
            current = prev.next
            prev.next = current.next
            return current.data
            
            




            



            
            
            
        


            
        


                










    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        listr = ''

        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next 
        print(listr)


if __name__ == "__main__":
    linkedlst = LinkedList()
    linkedlst.addFirst(5)
    linkedlst.addFirst(5)
    linkedlst.removeLast()
    linkedlst.addFirst(5)
    linkedlst.addLast(8)
    linkedlst.add(2,78)
    linkedlst.remove(2)
    
    
    
    linkedlst.print()





            