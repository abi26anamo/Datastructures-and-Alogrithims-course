class LinkedListIterator:
    def __init__(self,head):
        self.curr =head
    def __next__(self):
        if self.curr  == None:
            raise StopIteration
        data = self.curr.Data
        self.curr = self.curr.Next
        return data