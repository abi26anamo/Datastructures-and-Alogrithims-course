from linkedlist import LinkedList
class Queue:
    def __init__(self):
        self.element = LinkedList()

    def enque(self,e):
        self.element.insert_at_end(e)
    def deque(self):
        if self.getSize() == 0:
            return None
        else:
            return self.element.remove(0)
    def getSize(self):
        return len(self.element)
    def isEmpty(self):
        return len(self.element)==0
    def __str__(self):
        return self.element.__str__()

if __name__ == "__main__":
    queue = Queue()
    for i in range(10):
        queue.enque(i)
    while not queue.isEmpty():
        print(queue.deque())