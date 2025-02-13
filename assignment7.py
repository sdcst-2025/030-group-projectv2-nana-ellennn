#!python3
#Geometric sequence calculator
def title():
    print('Welcome to Geometric sequence calculator')
    print('Here is the Geometric sequence: 2,4,8,16,......')
    print("You can enter a number representing nth term to find out the actual number in this term .")

def main():
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

if __name__ == "__main__":
    title()
    main()