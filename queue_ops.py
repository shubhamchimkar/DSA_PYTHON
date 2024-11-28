import array

"""
Class Queue:
    Implementing the queue data structure
"""


class Queue:
    """
    Queue Class
    """
    def __init__(self):
        """
        Constructor
        """
        # initializing the queue
        self.my_queue = array.array('i', [])
        self.front = -1


    def get_front(self):
        """
        Returns the front element of the Queue
        """
        if self.is_empty():
            print("Queue is empty, no front element.")
        else:
            # return the front element
            print(self.my_queue[0])


    def get_rear(self):
        """
        Returns the rear element of the Queue
        """
        if self.is_empty():
            print("Queue is empty, no rear element.")
        else:
            # return the rear element
            print(self.my_queue[-1])


    def is_empty(self):
        """
        Checks whether the Queue is empty or not
        """
        if len(self.my_queue):
            return False
        else:
            return True


    def enqueue(self, element):
        """
        Adds an element to the rear of the Queue
        """
        # add the element at the end of the queue
        self.my_queue.append(element)
    
    def dequeue(self):
        """
        Removes an element from the front of the Queue
        """
        if self.is_empty():
            print("Queue is empty can't dequeue")
        else:
            # remove the element from the front of the queue
            self.my_queue.pop(0)
    
if __name__ == "__main__":
    queue = Queue()
    print(queue.my_queue)
    queue.get_front()
    queue.enqueue(1)
    queue.get_front()
    queue.get_rear()
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.my_queue)

    queue.dequeue()
    queue.get_front()
    queue.get_rear()
    queue.dequeue()
    queue.dequeue()
    
    print(queue.my_queue)
    queue.dequeue()

