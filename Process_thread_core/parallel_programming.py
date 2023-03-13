import os
import multiprocessing

def Square(No):
    print("PID of worker process is{} for input {}".format(os.getpid(),No))
    return (No*No)

def main():
    print("Process ID of our application is:",os.getpid())

    data=[1,2,3,4,5]
    Result=[]

    pobj=multiprocessing.Pool()
    Result=pobj.map(Square,data)

    print("Result after square operation is:",Result)

if __name__=="__main__":
    main()