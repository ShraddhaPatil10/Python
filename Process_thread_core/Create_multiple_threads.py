# Multiprocessing---> Create multiple threads
# Parallel Programming

import time
import threading


def DisplayEven(no):
    for i in range(no):
        if (i % 2 == 0):
            print("Even number:", i)


def DisplayOdd(no):
    for i in range(no):
        if (i % 2 != 0):
            print("Odd number:", i)


def main():
    print("Demonstration of parallel programming using multiple process")

    number = 2000
    p1 = threading.Thread(target=DisplayEven, args=(number,))
    p2 = threading.Thread(target=DisplayOdd, args=(number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()

    print("Execution time is:", end_time - start_time)
