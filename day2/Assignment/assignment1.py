var_1 = input('First number = ')
var_2 = input('What do you want to do? ') 
var_3 = input('Second number = ')

if (var_2 == '+') :
    print(f'The answer is {int(var_1) + int(var_3)}') 
elif (var_2 == '-') :
    print(f'The answer is {int(var_1) - int(var_3)}')
elif (var_2 == '*') :
    print(f'The answer is {int(var_1) * int(var_3)}')
elif (var_2 == '/') :
    print (f'The answer is {int(var_1) / int(var_3)}')
else:
    print('error')