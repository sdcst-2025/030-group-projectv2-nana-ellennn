#!python3
#Work calculator
def title():
    print('Welcome to Work calculator')
    print("You can calculate how much work you have done after an action in physics.")
    print("Please enter values for mass and distance.")

def main():
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

if __name__ == "__main__":
    title()
    main()