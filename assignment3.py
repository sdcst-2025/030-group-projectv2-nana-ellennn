def title():
    print('Welcome to globular volume calculator')
    print('You can calculate globular volume')

def main():
    title()
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

if __name__=="__main__":
    main()
                