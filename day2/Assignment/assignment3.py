user_input = input('Pick a number ')

if (int(user_input) % 3 == 0) and (int(user_input) % 5) == 0:
    print('Fizz Buzz')
elif (int(user_input) % 3) == 0:
    print ('Fizz')
elif  (int(user_input) % 5) == 0:
    print ('Buzz')
else:
    print('idk what to do now')
 