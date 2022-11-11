def Area(Radius,PI=3.14):
    Res=PI*Radius*Radius
    return Res

def main():
    Rvalue=10.5
    PIvalue=3.14

    Ans=Area(Rvalue,PIvalue)                #Positional Arguments
    print("Area of circle is:",Ans)

    Ans=Area(Radius=Rvalue,PI=PIvalue)      #Keyword Arguments
    print("Area of circle is:",Ans)

    Ans=Area(10.5)                          #Positional+Default
    print("Area of circle is:",Ans)

    Ans=Area(Radius=10.5)                   #Keyword+Default
    print("Area of circle is:",Ans)

    Ans=Area(PI=7.10,Radius=10.5)
    print("Area of circle is:",Ans)
    
if __name__=="__main__":
    main()