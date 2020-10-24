duckPerc = 0
Yes = 'Yes'
No = 'No'

#Question 1

q1 = input('Do you have feathers?(Yes or No): ')
if q1 == 'Yes':
    duckPerc+= 20
elif q1 == 'No':
    duckPerc += 0
else:
    print(input('Please say Yes or No: '))
    
#Question 2

q2 = input('Do you have a corkscrew penis?(Yes or No): ')
if q2 == 'Yes':
    duckPerc += 20
elif q2 == 'No':
    duckPerc += 0
else:
    print(input('Please say Yes or No: '))

#Question 3

q3 = input('Do you caw?(Yes or No): ')
if q3 == 'Yes':
    duckPerc += 0
elif q3 == 'No':
    duckPerc +=20
else:
    print(input('Please say Yes or No: '))

#Question 4

q4 = input('Have you gone quackers?(Yes or No): ')
if q4 == 'Yes':
    duckPerc += 0
elif q4 == 'No':
    duckPerc += 20
else:
    print(input('Please say Yes or No: '))

#Question 5
q5 = input('Are you being watched?(Yes or No): ')
if q5 == 'Yes':
    duckPerc += 20
elif q5 == 'No':
    duckPerc += 0
else:
    print(input('Please say Yes or No: '))

if duckPerc:
    print(f"You are {duckPerc}% Duck.")
else:
    print("You are not a duck")
