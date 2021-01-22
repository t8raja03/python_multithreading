## Operating System Basics and Multithreading with Python, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 3

import threading

count = 0
lock = threading.Lock()
threads = []

def increment_count():
    global count
    with lock:
        count += 1
        print("Hello World: " + str(count))


def main():
        thread = threading.Thread(target=hello_world, args=())
        threads.append(thread)
        thread.start()

def hello_world():
    while count < 100:
        increment_count()

if __name__ == '__main__':
    main()
