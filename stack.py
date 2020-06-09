class stack:
    def __init__(self,m):
        self.m = m
        self.s = []

    def IsEmpty(self):
        if self.s == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.s) == self.m:
            return True
        return False
    
    def push(self,value):
        if self.isFull():
            print("Stack is Full")
        else:
            self.s.append(value)

    def pop1(self):
        if(self.IsEmpty()==True):
            print("Stack is Empty ")
        else:
            self.s.pop()

    def display(self):
        print(self.s)

    def peek(self):
        if not self.IsEmpty == []:
            return self.s[-1]

    def IB(self):
        for i in self.s:
            print(bin(i),end = ' ')
            

    def size(self):
        print('stack has',len(self.s),'Elements')

    def sort(self):
        print(self.s.sort())

if __name__=="__main__":
    
    while(True):
        obj = stack(2)
        obj.push(12)
        obj.push(10)
        obj.push(9)
        obj.push(80)
        obj.display()
        #obj.IB()
        break
        '''obj.sort()
        obj.size()
        obj.display()
        obj.pop1()
        obj.display()
        obj.pop1()
        obj.display()
        obj.pop1()
        obj.push(20)
        obj.push(192)
        obj.push(252)
        obj.push(19)
        print(obj.IB())
        print(obj.peek())
        break
        '''
        
