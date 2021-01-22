## Operating System Basics and Multithreading with Python, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 3

## This program uses multiple threads to print 'Hello World from thread <thread>: count=<count>'
## The idea is to increment the global variable count and still print the Hello Worlds in
## sequential order regardless of how many threads are trying to increment the count-variable.
## The program also prints additional information indented, like which thread is trying to acquire
## a lock at which time.

import threading    # Import the threading module
import time         # used to calm down printing to console

NUMBER_OF_THREADS = 5   # Number of threads to start
COUNT_MAX = 20          # Number of times count is incremented

count = 0           # The global variable all threads are trying to increment simultaneously
lock = threading.Lock() # variable for the Lock object
threads = []        # Array to hold the threads and their status

# ANSI escape codes to make console text italic
# Might not work an all terminals, if these get printed out and the Hello Worlds are not italic,
# change them to empty strings or remove the 'it + ' and 'end_it' from line 39
# Source: https://stackoverflow.com/questions/13559276/can-i-write-italics-to-the-python-shell#13559470
it = '\x1B[3m'
end_it = '\x1B[23m'

# The function to increment the count-variable
def increment_count(thread_number):
    global count    # Inform to use the global variable
    # Print information on which thread is waiting for its turn to increment count
    print("     Thread " + str(thread_number) + " trying to acquire lock...")
    # The with -statement is basically a try-catch, it first tries is lock is acquired,
    # and if not, keeps trying again. Only when the lock is acquired is the code within executed
    with lock:
        # Inform which thread acquired the lock
        print ("     Thread " + str(thread_number) + " acquired Lock!")
        count += 1
        # Print the Hello World with thread information
        # This is the whole point of this exercise, 'count' should increment sequentially
        print(it + "\nHello World from thread " + str(thread_number) + ": count=" + str(count) + "\n" + end_it)
        time.sleep(1/100)   # This is used to calm the terminal output and keep it more readable
                            # parallel threads tend to write on the same line

    # Inform which thread released the lock
    print("     Thread " + str(thread_number) + " released lock")

# main()-function starts the threads
def main():
    # informational
    print("\n\nStarting main(), count=" + str(count) + "\n\n")
    # Start the threads
    for j in range(NUMBER_OF_THREADS):
        # Each loop creates a thread object targeting hello_world-function and passing
        # the iterator as a parameter, then adds the thread object to the list containing
        # the thread objects
        thread = threading.Thread(target=hello_world, args=(j,))
        threads.append(thread)
        thread.start()
        print("+    Started thread " + str(j))
    # informational
    print("\n\nFinished main()\nStarted " + str( len(threads) ) + " threads\n\n")
    time.sleep(1/100)   # Calm the terminal output a little

# hello_world() is the target function for the threads
def hello_world(thread_number):
    # keep incrementing count until COUNT_MAX
    # Example: COUNT_MAX = 10, NUMBER_OF_THREADS = 5:
    # Before count gets to 10, all the threads pass and go to function increment_count().
    # When count=9, the thread passes on, but there are the other 4 threads that
    # have passed previously and are already waiting to increment 'count'. After the last pass,
    # all those 4 threads waiting plus the last thread passing will increment 'count', so
    # the final value will be 9+5=14 (COUNT_MAX-1 + NUMBER_OF_THREADS). 
    # When NUMBER_OF_THREADS is substracted from COUNT_MAX, COUNT_MAX will be the number of 
    # 'Hello Worlds' printed (COUNT_MAX-1 + NUMBER_OF_THREADS - NUMBER_OF_THREADS, the first
    # Hello World is printed with count=0)
    while count < COUNT_MAX - NUMBER_OF_THREADS:
        print("     Thread " + str(thread_number) + " @ hello_world(), count=" + str(count))
        increment_count(thread_number)
    # When the above check is False, the thread can end
    print("-    Thread " + str(thread_number) + " finished!")

if __name__ == '__main__':
    main()
