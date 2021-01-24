## Operating System Basics and Multithreading with Python, spring 2021
 Jarno Rankinen TVT19KMO
## Report

The three exercises were simple examples of handling multithreading with Python.
The main challenge for me was the Python language, I had used it only very
little prior to this course. It seems that Python offers good built-in ways to
handle multiple threads, in comparison to some other languages I had
used before.

The most interesting part in the course and the exercises was the various prob-
lems multiple threads cause, such as race conditions and general issues with
threads accessing shared recourses. I had heard of these problems before, but
had not had the chance to get practice with them. Overall the course provided a 
good introduction to the basics in the topic.

Exercise #1 is a simple program that simply creates a bunch of threads, each
printing out `Hello World from thread #N`, where N is the number of the thread
which is assigned in order the threads are created. While this program prints
the numbers in order most of the time, after executing the program roughly 50
times I saw how this is not always the case.

Exercise #2 is very similar to #1, but the threads are created using a custom 
subclass of `threading.Thread`. Again, most of the time the numbers were printed
to the console consecutively, but there were some instances where the order was
mixed up.

Exerise #3 also does the same thing, but introduces a global variable `count` 
that each thread increments. Access to the `count` variable is controlled with 
a simple lock. The output from each thread is e.g.

    Hello World from thread 3: count=5
where the number of the thread and the value of `count` obviously varies.
In addition I added debugging or informational output, e.g.

    -    Thread 0 finished!
         Thread 1 released lock
    -    Thread 1 finished!
         Thread 3 acquired Lock!
to have a better understanding of what is happening in the execution. This
exercise showed very well how multiple threads behave, and in many occasions
the same thread that released the lock was also the next one to acquire it, even
though all the threads were waiting to acquire the lock.