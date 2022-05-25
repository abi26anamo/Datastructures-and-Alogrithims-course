class Stack:
    def __init__(self):
        self.__data = []

    def isEmpty(self):
        return len(self.__data) == 0
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__data[-1]
    def push(self,value):
        self.__data.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__data.pop()
    def getSize(self):
        return len(self.__data)

if __name__ == "__main__":
    stack = Stack()

    for i in range(10):
        stack.push(i)
    while not stack.isEmpty():
         print(stack.pop())
    

        

