
# Question 1
# Implement a stack using a list in Python. Include the necessary methods such as push, pop, and isEmpty.


# Stack Creation
class Stack:
    def __init__(self):
        self.items = list()

# Checking for empty stack
    def isEmpty(self):
        return self.items == []
# Inserting elements into the stack
    def push(self, item):
        print("item pushed is: " + str(item))
        self.items.append(item)

# To remove element from the stack
    def pop(self):
        if (self.isEmpty()):
            return "stack is empty"
        else:
            return self.items.pop()


        
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.pop()
print(stack.pop())
