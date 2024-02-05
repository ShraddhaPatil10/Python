class Animal:
    print("I'm in Animal class")

class Pet(Animal):
    print("I'm in Pet class")

class Dog(Pet):
    def Bark(self):
        print("Dog is barking")

def main():
    obj1=Animal()

    obj2=Pet()

    obj3=Dog()
    obj3.Bark()

if __name__=="__main__":
    main()

