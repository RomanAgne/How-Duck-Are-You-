duckPerc = 0
Yes = 'Yes'
No = 'No'

#Question 1

q1 = input('Do you have feathers?(Yes or No): ')
if q1 == 'Yes':
    Yes == True
    duckPerc+= 20
elif q1 == 'No':
    No == False
    duckPerc += 0
else:
    print(input('Please say Yes or No: '))
    
#Question 2

q2 = input('Do you have a corkscrew penis?(Yes or No): ')
if q2 == 'Yes':
    Yes == True
    duckPerc += 20
elif q2 == 'No':
    No == False
    duckPerc += 0
else:
    print(input('Please say Yes or No: '))

#Question 3

q3 = input('Do you caw?(Yes or No): ')
if q3 == 'Yes':
    Yes == False
    duckPerc += 0
elif q3 == 'No':
    No == True
    duckPerc +=20
else:
    print(input('Please say Yes or No: '))

#Question 4

q4 = input('Have you gone quackers?(Yes or No): ')
if q4 == 'Yes':
    Yes == False
    duckPerc += 0
elif q4 == 'No':
    No == True
    duckPerc += 20
else:
    print(input('Please say Yes or No: '))

#Question 5
q5 = input('Are you being watched?(Yes or No): ')
if q5 == 'Yes':
    Yes == True
    duckPerc += 20
elif q5 == 'No':
    No == False
    duckPerc += 0
else:
    print(input('Please say Yes or No: '))

class Duck:
    if duckPerc == 100:
        print('You are 100% Duck.')
    elif duckPerc == 80:
        print('You are 80% Duck.')
    elif duckPerc == 60:
        print('You are 60% Duck.')
    elif duckPerc == 40:
        print('You are 40% Duck.')
    elif duckPerc == 20:
        print('You are 20% Duck.')
    else:
        print('You are not a Duck.')
