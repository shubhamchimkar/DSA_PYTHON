import array

class Queue:
    def __init__(self):
        self.my_queue = array.array('i', [])
        self.front = -1

    def get_front(self):
        if self.is_empty():
            print("Queue is empty, no front element.")
        else:
            print(self.my_queue[0])

    def get_rear(self):
        if self.is_empty():
            print("Queue is empty, no rear element.")
        else:
            print(self.my_queue[-1])

    def is_empty(self):
        if len(self.my_queue):
            return False
        else:
            return True

    def enqueue(self, element):
        self.my_queue.append(element)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty can't dequeue")
        else:
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
