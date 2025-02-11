def title():
    print('Welcome to use Angle Calculater')
    print('You can convert between Radians and degrees')

def main():
    title()
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
 
if __name__=="__main__":
   main()
    
   
