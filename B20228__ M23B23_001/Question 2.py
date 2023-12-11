# give the class a name
class StudentQueue:
    def __init__(self):#initialize the class
        self.queue = []

    def enqueue(self, student):#initialize the enqueue
        self.queue.append(student)

    def dequeue(self):#initialize the dequeue
        if not self.is_empty():#introduce an if statement
            return self.queue.pop(0)
        else:
            return "Queue is empty."

    def is_empty(self):#initialize the is_empty(find out if clss is empty)
        return len(self.queue) == 0


    def queue_size(self):#initialize the queue_size(to find out the size)
        return len(self.queue)


# An example would be:
student_queue = StudentQueue()

student_queue.enqueue("Steven")# names of students
student_queue.enqueue("Joy")
student_queue.enqueue("Mark")

print(student_queue.queue)  # Output: ['Steven','Joy','Mark']

served_student = student_queue.dequeue()
print("Served Student:", served_student)  # Output: Served Student: Steven

print("Is the queue empty?", student_queue.is_empty())  # Output: Is the queue empty? False

print("Current queue size:", student_queue.queue_size())  # Output: Current queue size: 2