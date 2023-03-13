import multiprocessing
import os

def Square(n):
    print("Worker process id for {0}:{1}".format(n,os.getpid()))

if __name__=="__main__":
    arr=[1,2,3,4,5]

    #Creating a pool object
    p=multiprocessing.Pool()

    #Map list to target function
    result=p.map(Square,arr)

    print("Square of each elements:")
    print(result)