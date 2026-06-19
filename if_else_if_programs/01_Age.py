age = int(input('enter your age: '))

if age <= 13:
    print ("Child")
elif age <= 18 :
    print ("Teenager")
elif age <= 50 :
    print ("Adult")
else:
    print ("Senior Citizen")