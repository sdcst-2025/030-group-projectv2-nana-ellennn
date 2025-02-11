#!python3
# Volume Calculator
# Feel free to rename your variables

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    print('Copper Valume Calculator\nWelcome to use!')
    print('This program is for calculating the volume of Copper in STP(standard tempreture and pressure)')
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: 
    # Modified:
    print('When Copper in STP, 1mole=22.4L.\nWe can calculate it by the mass of Copper \nthe moleculars of Copper \nthe mole of Copper')
    return None



def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()
    while True:
        # keep giving options to choose menu options until they choose to exit
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
      
  

if __name__ == "__main__":
    instructions()
    main()

