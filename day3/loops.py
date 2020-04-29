#Loops

names = ["John", "Jane", "Mary", "Mike"]

for name in names:
    print(f'{name} Smith')

def add(x, y):
    return x + y

numbers_to_add = [[2, 3], [2 ,4], [2, 7], [1, 0], [2, 8], [2, 3]]

for numbers in numbers_to_add:
    print(add(numbers[0], numbers[1]))

for i in range(2, 100, 2): # range(start, stop, skip)
    print(i)

is_active = True

while is_active:
    print('hello world')
    is_active = False

total = 10 
stepper = 0

while stepper < total: 
    print(f'Step {stepper}')
    stepper = stepper + 1
print('done')


sentence="Loops are hard"
vowels=0 
for i in sentence:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels=vowels+1
print(f'{sentence} has {vowels} vowels.')
