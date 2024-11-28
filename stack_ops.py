import array

class Stack:
    """
    Stack class
    """
    def __init__(self):
        """
        Constructor
        """
        self.my_stack = array.array('i', []) #stack is an array
        self.top = -1 #top is the index of the top element in stack

    def get_top(self):
        """
        Returns the index of the top element in the stack
        """
        print(len(self.my_stack)-1)
    
    def is_empty(self):
        """
        Checks whether the stack is empty or not
        """
        if len(self.my_stack):
            return False
        else:
            return True
        
    def push(self,element):
        """
        Adds an element to the top of the stack
        """
        self.my_stack.append(element)

    def pop(self):
        """
        Removes an element from the top of the stack
        """
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
