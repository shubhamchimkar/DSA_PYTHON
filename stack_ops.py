import array

class Stack:
    def __init__(self):
        self.my_stack = array.array('i', [])
        self.top = -1

    def get_top(self):
        print(len(self.my_stack)-1)
    
    def is_empty(self):
        if len(self.my_stack):
            return False
        else:
            return True
        
    def push(self,element):
        self.my_stack.append(element)

    def pop(self):
        if self.is_empty():
            print("Stack is empty can't Pop")
        else:
            self.my_stack.pop()

if __name__ == "__main__": #entry point of the programm
    stack= Stack() #object in python

    print(stack.my_stack)
    stack.get_top()

    stack.push(1)
    stack.get_top()
    stack.push(2)
    stack.get_top()
    stack.push(3)

    print(stack.my_stack)

    stack.pop()

    print(stack.my_stack)


