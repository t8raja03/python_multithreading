## Operating System Basics and Multithreading with Python, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 1

import threading

def hello_world(number):
    print ("Hello, World from thread #" + str(number + 1))

threads = []

for j in range(10):
    thread = threading.Thread(target=hello_world, args=(j,))
    threads.append(thread)
    thread.start()