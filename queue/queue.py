"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# Initialize Queue with an array

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) == 0:
            return
        else:
            item = self.storage[0]
            self.storage.remove(self.storage[0])
            return item

# Initialize Queue with a linked list

from ..singly_linked_list.singly_linked_list import *

class Queue:
    def __init__(self):
        pass

    def __len__(self):
        pass

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass
