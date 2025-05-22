name = str(input('Your name: '))
weight = int(input("Weight in Kg: "))
height = int(input("Height in Cm: "))


BMI = weight / (height/100)**2
print(BMI)

if BMI>0:
    if(BMI<18.5):
        print('underweight')
    elif(BMI<24,9):
        print('normal')
    elif(BMI<29,9):
        print('obese')
    elif(BMI<39,9):
        print('severly obese')
    elif(BMI>40):
        print('bro go to the gym')
else:
    print('Please enter valid input')