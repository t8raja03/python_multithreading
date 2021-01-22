## Operating System Basics and Multithreading with Python, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 2

import threading

class HelloWorldThread(threading.Thread):
    def __init__(self, number):
        super(HelloWorldThread, self).__init__()
        self.number = number

    def run(self):
        print("Hello World from thread #" + str(self.number + 1))

threads = []

for j in range(10):
    thread = HelloWorldThread(j)
    threads.append(thread)
    thread.start()  


