## Operating System Basics and Multithreading with Python, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 2

## This program does the exact same thing as Example 1, but uses its own
## subclass of the threading.Thread class to do the execution.

import threading        # Import the threading module

# HelloWorldThread is a subclass of threading.Thread -class
class HelloWorldThread(threading.Thread):
    # Override the __init__-function
    def __init__(self, number):
        super(HelloWorldThread, self).__init__()
        self.number = number    # set value of the class member 'number'
                                # according to the argument passed

    # run() is the executing function of the threading.Thread -class
    def run(self):
        # Print out 'Hello World from thread #<number>
        print("Hello World from thread #" + str(self.number + 1))

# Initialize an array to hold the HelloWorldThread-objects
threads = []

# In each loop a HelloWorldThread object is created with the iterator
# of the for-loop passed to it as an argument, the HelloWorldThread is
# appended to the threads-array and the thread is started.
for j in range(10):
    thread = HelloWorldThread(j)
    threads.append(thread)
    thread.start()  


