#!python3
# Surface Area Calculator
import math

def title():
    print("Welcome to cone surface area calculator!")
    print("This calculator is used to find out the surface area of cone.")
    print("Please enter values for radius and slant height.")

def main():
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

if __name__ == "__main__":
    title()
    main()