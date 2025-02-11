#!python3
# Volume Calculator
import math

def title():
    print("Welcome to cone and cylinder volume calculator!")
    print("This calculator can calculate the volume of cone and cylinder.")
    print("Please enter two values for radius and height.")
   
def main():
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


if __name__ == "__main__":
    title()
    main()