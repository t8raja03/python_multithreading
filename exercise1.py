## Operating System Basics and Multithreading with Python, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 1

## This program simply creates a bunch of threads that print out 
## 'Hello, World from thread #<thread number>'

import threading            # Import the threading module

# We'll define a function that prints out the text:
def hello_world(number):
    print ("Hello, World from thread #" + str(number + 1))

# Initialize an empty array to hold the Thread objects
# so their status can be tracked
threads = []

# In each loop a new Thread object is created, the function
# 'hello_world' is passed as the target to the Thread
# object, the iterator of the for-loop is passed as the
# argument to the hello_world-function, and the thread is
# started
for j in range(10):
    thread = threading.Thread(target=hello_world, args=(j,))
    threads.append(thread)
    thread.start()