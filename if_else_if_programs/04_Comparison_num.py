num1 = int(input('Enter 1st number : '))
num2 = int(input('Enter 2nd number : '))
num3 = int(input('Enter 3rd number : '))

if num1 == num2 and num2 == num3:
    print ("All Numbers are Equal")
elif num2 == num3:
    print ("2nd and 3rd Numbers are Equal")
elif num1 == num3:
    print ("1st and 3rd Numbers are Equal")
elif num1 == num2:
    print ("1st and 2nd Numbers are Equal")
elif num1 > num2 and num1 > num3:
    print ("1st Number is Largest : ", num1)
elif num2 > num1 and num2 > num3:
    print ("2nd  Number is Largest : ", num2)
elif num3 > num1 and num3 > num2:
    print ("3rd Number is Largest : ", num3)
    

    
