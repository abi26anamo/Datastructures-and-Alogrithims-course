class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right = None

class BST:
    def __init__(self):
        self.__root = None
        self.__size = 0
    def get_root(self):
        return self.__root
    def insert(self,data):
        if self.__root ==None:
            self.__root = BSTNode(data)
        current = self. __root
        parent = None
        while current !=None:
            parent =current
            if data < current.data:
                current= current.left
            elif data > current.data:
                current = current.right
            else:
                False
        if parent.data < data:
            parent.right = BSTNode(data)
        else:
            parent.left =BSTNode(data)
        self.__size+=1
        return True
    def search(self,data):
        if self.__root == None:
            return False
        else:
            current = self.__root
            while current != None:
                if current.data < data:
                    current = current.right
                if current.data > data:
                    current = current.left
                else:
                    return True
            return False
    def inorder(self,root):
        if self.root != None:
            self.inorder(root.left)
            print(root.data,end="")
            self.inorder(root.right)
            


    def getSize(self):
        return self.__size
        
def main():
    bst = BST()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.inorder()
    
    


main()