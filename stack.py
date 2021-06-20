class Stack:
    def __init__(self):
        self.book = []
    
    def push(self, bname):
        self.book.append(bname)
    def pop(self):
        return self.book.pop()
    def isEmpty(self):
        if self.book == []:
            return True
        else:
            return False
    def peek(self):
        return self.book[len(self.book) - 1]

    def printStack(self):
        self.book.reverse()
        for i in self.book:
            print(i)
        self.book.reverse()

    def __str__(self):
        self.book.reverse()
        
     
        p = "\n".join(self.book)
        self.book.reverse()
        return p
        
