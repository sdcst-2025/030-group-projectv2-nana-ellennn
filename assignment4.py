def title():
    print('Welcome to Interest calculator')
    print('You can calculate Interest')
    print('You can test this program by (p,r,n,t)=(1000,4,4,2)')

    print('Welcome to globular Interest calculator')
    print('You can calculate Interest volume')
    print('You can test this program by (p,r,n,t)=(1000,4,4,2)\nThe answer should be 1082.86')


def main():
    title()
    while True:
        try:
          P=float(input("Enter your principal:"))
          r=float(input('Enter your rate:'))
          n=float(input('Enter your # of compounding periods per year:'))
          t=float(input('Enter your # of year:'))
          A=P*(1+(r/100)/n)**(n*t)
          A=round(A,2)
          print(A)
        except:
            print("Please enter a number")
            return True
        
if __name__=="__main__":
    main()