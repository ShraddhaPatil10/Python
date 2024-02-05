class c2vec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class c3vec(c2vec):
    def __init__(self, i, j,k):
        super().__init__(i,j)
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


def main():
    obj1=c2vec(1,3)
    print("2 dimensional vector is:",obj1)

    obj2=c3vec(1,5,7)
    print("3 dimensional vector is:",obj2)


if __name__=="__main__":
    main()