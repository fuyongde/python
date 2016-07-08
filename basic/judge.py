s = input("age:");
age = int(s);
if age >= 18:
    print('Your age is ', age);
    print('adult');
elif age >= 6:
    print('Your age is ', age);
    print('teenager');
else:
    print('kid');