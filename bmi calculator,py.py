# we are now making bmi calculator
height = float(input("enter your height in cm"))
weight = float(input("enter your weight in kg"))
height_m = height/100
bmi = weight/height_m**2
if bmi < 18 :
    print(" you are underweight and your bmi is " + str(round(bmi,2)))
elif bmi < 25 :
    print( 'you are normal and your bmi is ' + str(round(bmi,2)))
else :
    print('you are overweight' + str(round(bmi,2)))