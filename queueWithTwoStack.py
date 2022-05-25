
from stack import Stack
class StackQueue:

    def __init__(self) :
        self.__stack1 = Stack()
        self.__stack2 = Stack()
    def enque(self,value):
        self.__stack1.push(value)
    def deque(self):
        if self.__stack2.getSize()==0:
            if self.__stack1.getSize() == 0:
                return None
            while self.__stack1.getSize() > 0:
                last_of_stack1 = self.__stack1.pop()
                self.__stack2.push(last_of_stack1)
        return self.__stack2.pop()
def main():
    myqueue = StackQueue()
    myqueue.enque(23)
    myqueue.enque(34)
    myqueue.enque(45)
    myqueue.enque(67)
    print(myqueue.deque())
    print(myqueue.deque())
    print(myqueue.deque())
    myqueue.enque(88)
    print(myqueue.deque())
    print(myqueue.deque())
    
main()

# hoof man algorithim