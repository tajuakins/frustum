# frustum.py
# Program to calculate volume
# of frustum of a cone
# by : Akinosho Tajudeen

import math  
def volume1():
    r = int(input("Enter the upper radius (r): "))
    R = int(input("Enter the lower radius (R): "))
    h = int(input("Enter the height of small cone(h): "))
    H = int(input("Enter the height of big cone (H): "))
    volFrustum = 1 / 3 * (math.pi * (R * R * H - r * r * h))
    print ("\nThe solutions is:", round(volFrustum,3)) 


def volume2():
    r = int(input("Enter the upper radius (r): "))
    R = int(input("Enter the lower radius (R): "))
    h = int(input("Enter the height of the frustum (h): "))  
    volFrustum = 1 / 3 * (math.pi * h * (r * r + r * R + R * R ))
    print ("\nThe solutions is:", round(volFrustum,3)) 


def main():
    print("\nSelect 1 for Vol = 1 / 3 * (math.pi * (R * R * H - r * r * h ))")
    print("\nSelect 2 for Vol = 1 / 3 * (math.pi * h * (r * r + r * R + R * R ))")
    select = int(input("\nSelect the appropriate number :"))
    if select == 1:
        volume1()
    if select == 2:
        volume2()
    else:
        print("\nSelect 1 or 2")
    


play = 'yes' 
while play == 'yes' or play == 'y':
    main()
    print('Do you want to calculate another volume? (yes or no)')
    play = input('\n** ')











    
