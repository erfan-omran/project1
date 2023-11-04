i = 0

while i < 10:
    _list =[]
    for item in range(50):
        _list.append(item) # Add item to list
    
    print(f'list {i + 1}') # Print list's count

    for item in _list:
        print(item + 1) # Print indexes

    i += 1

#---------------------------------------------------

for i in range(1 , 3001):
    print(i)

#---------------------------------------------------

avg = 0
corse = 10

while avg < 20:
    avg = 0
    
    print('If you can pass your exam with 20 score we have a gift for you!')

    for i in range(10):
        quiz_score = int(input('Enter your quiz score : ')) # Gereftan nomarat as user
        avg += quiz_score 
    avg /= corse # Mohasebe avg

print('Happy new bike')

#---------------------------------------------------

password = input('Enter your password : ')
repeat_password = input('Repeat your password : ')

while password != repeat_password:
    print('Erorr \n    your password repeat is incorrect pls try again')
    repeat_password = input('Repeat your password again : ')

print('Your password is correct!')