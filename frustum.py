# frustum.py
# Program to calculate volume
# of frustum of a cone
# by : Akinosho Tajudeen

import math  
def volume():
    r = int(input("Enter the upper radius (r): "))
    R = int(input("Enter the lower radius (R): "))
    h = int(input("Enter the height of the frustum (h): "))  
    volFrustum = 1 / 3 * (math.pi * h * (r * r + r * R + R * R ))
    print ("\nThe solutions is:", round(volFrustum,3)) 

play = 'yes'
while play == 'yes' or play == 'y':
    volume()
    print('Do you want to calculate another volume? (yes or no)')
    play = input('\n** ')

