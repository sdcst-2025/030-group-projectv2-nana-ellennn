import math
runProgram = True

def runP1():
    print("Welcome to cone and cylinder volume calculator!")
    print("This calculator can calculate the volume of cone and cylinder.")
    print("Please enter two values for radius and height.")
    while True:
         try:
            r=float(input("Enter values for radius: "))
            h=float(input("Enter values for height: "))
            a=int(input("Enter 0 to calculate the volume of cone(any other numbers if don't) : "))
            b=int(input("Enter 1 to calculate the volume of cylinder(any other numbers if don't): "))
            c=int(input("Enter 2 to calculate the volume of cone and cylinder with the same base and height(any other numbers if don't): "))
            if a==0 and b!=1 and c!=2:
                v=1/3*math.pi*r**2*h
                v=round(v,2)
                print(f"The volume of cone is {v}")
                    #return True
            if b==1 and a!=0 and c!=2:
                v=math.pi*r**2*h
                v=round(v,2)
                print(f"The volume of cylinder is {v}")
                    #return True
            if a!=0 and b!=1 and c==2:
                v=1/3*math.pi*r**2*h
                v=round(v,2)
                print(f"The volume of cone is {v}")
                v=math.pi*r**2*h
                v=round(v,2)
                print(f"The volume of cylinder is {v}")
                    #return True
         except:
            print("Please enter valid values!")
            return True
    pass
def runP2():
    print('Welcome to use Angle Calculater')
    print('You can convert between Radians and degrees')
    while True:
      try:
        R=float(input('Enter you radians (if u don\'t want to calculate by it, enter 0):'))
        D=float(input('Enter you degrees (if u don\'t want to calculate by it, enter 0):'))
        if R==0 and D!=0:
           x=D*(3.14/180)
           x=round(x,2)
           print(f'The radian is {x}')
           #return x
           #continue
        if D==0 and R!=0:
           y=R*(180/3.14)
           y=round(y,2)
           print(f'The degrees is {y}')
           #return True
           continue
        if D!=0 and R!=0:
           print('Please only enter one value that except 0')
           print('Try again')
           #return False
           #continue
        if D==0 and R==0:
           print('Please only enter one value that except 0')
           print('Try again')
      except:
           print('Please only enter number\nTry again')
           return True
    pass
def runP3():
    print('Welcome to globular volume calculator')
    print('You can calculate globular volume')
    while True:
        try:
          r=float(input('Enter your radius:'))
          V=4/3*3.14*(r**3)
          V=round(V,2)
          print(V)
          #return True
        except:
            print('Enter a number please')
            return True
    pass
def runP4():
    print('Welcome to Interest calculator')
    print('You can calculate Interest')
    print('You can test this program by (p,r,n,t)=(1000,4,4,2)')
    while True:
        try:
          P=float(input("Enter your principal:"))
          r=float(input('Enter your rate'))
          n=float(input('Enter your # of compounding periods per year'))
          t=float(input('Enter your # of year'))
          A=P*(1+(r/100)/n)**(n*t)
          A=round(A,2)
          print(A)
        except:
            print("Please enter a number")
            return True
    pass
def runP5():
    print("Welcome to cone surface area calculator!")
    print("This calculator is used to find out the surface area of cone.")
    print("Please enter values for radius and slant height.")
    while True:
         try:
            r=float(input("Enter values for radius: "))
            l=float(input("Enter values for slant height: "))
            SA=math.pi*r*(l+r)
            SA=round(SA,2)
            print(f"The surface area of the cone is {SA}")
            #return True
         except:
            print("Please enter valid values!")
            return True
    pass
def runP6():
    print('Welcome to Work calculator')
    print("You can calculate how much work you have done after an action in physics.")
    print("Please enter values for mass and distance.")
    while True:
         try:
            m=float(input("Enter values for mass in kg: "))
            d=float(input("Enter values for distance in m: "))
            g=9.81
            W=m*g*d
            W=round(W,2)
            print(f"The work done is {W}Nm")
            #return True
         except:
            print("Please enter valid values!")
            return True
    pass
def runP7():
    print('Welcome to Geometric sequence calculator')
    print('Here is the Geometric sequence: 2,4,8,16,......')
    print("You can enter a number representing nth term to find out the actual number in this term .")
    while True:
         try:
            n=int(input("Enter values for # of term: "))
            r=2
            term=2*r**(n-1)
            term=int(term)
            print(f"The {n} term is {term}")
            #return True
         except:
            print("Please enter valid values!")
            return True
    pass
def runP8():
    while True:
       try:
          Cm=float(input("enter the grams of Copper(if u don't want to calculate by mass, enter 0):"))
          Cmol=float(input("enter the mol of Copper(if u don't want to calculate by mol, enter 0):"))
          Cmolec=float(input("enter the moleculars of Copper(if u don't want to calculate by molecular, enter 0):"))
          print(Cm,Cmol,Cmolec)
  
          if Cmol==0 and Cmolec==0:
            V=Cm/63.55*22.4
            V=round(V,2)
            print(V)
                #return True
          elif Cm==0 and Cmolec==0:
            V=Cmol*22.4
            V=round(V,2)
            print(V)
                #return True
          elif Cm==0 and Cmol==0:
            V=Cmolec/(6.022*(10**23))*22.4
            print(V)
                #return True
       except:
            print('Please only enter one number that except 0')
            return True 
    pass


while runProgram == True:
    print("-------------------Welcome to Calculator Programs-----------------------")
    print("""
          1.Cone and Cylinder Volume Calculator
          2.Angle Calculater
          3.Circle Volume Calculater
          4.Interest Calculator
          5.Cone Surface Area Calculator
          6.Work Calculator
          7.Geometric Sequence Calculator
          8.Copper Volume Calculater
          """)
    # display menu

    #input statement get choice
    choice = input("Enter a number from 1 to 8 to run the program: ")
    if choice ==1:
        runP1()
    elif choice==2:
        runP2()
    elif choice==3:
        runP3()
    elif choice==4:
        runP4()
    elif choice==5:
        runP5()
    elif choice==6:
        runP6()
    elif choice==7:
        runP7()
    elif choice==8:
        runP8()    
    if choice == "Q":
        runProgram=False

if __name__ == "__main__":
    runP1()
    runP2()
    runP3()
    runP4()
    runP5()
    runP6()
    runP7()
    runP8()
