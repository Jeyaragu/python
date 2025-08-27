# Finding Odd or even number
# n = 18
# moduleN = n % 2
# if(moduleN > 0):
#     print('Weird')
# else:
#     if(n >= 2 and n <=5):
#         print('Not Weird')
#     elif(n >= 6 and n <=20 ):
#         print('Weird')
#     else:
#         print('Not Weird')

# Finding Vote eligibility
# age = int(input('Enter age:'))
# if age >= 18:
#     print('Eligible')
# else:
#     print('Not Eligible')

# Age Check for Work
# inputAge = int(input('Enter age of the person: '))
# if inputAge >= 18 and inputAge < 60:
#     print('Eligible for work ' + str(inputAge))
# else:
#     print('Not Eligible for work ' + str(inputAge))

# Valid Marks
# validMark = int(input('Enter the mark: '))
# if validMark > 0 and validMark <= 100:
#     print('Valid Mark ' + str(validMark))
# else:
#     print('Invalid Mark ' + str(validMark))    

# Gender Check
# genderInput = input('Enter M or F: ')
# if genderInput == 'M' or genderInput == 'm':
#     print('Gender is Male')
# else:
#     print('Gender is female')

# Vowels or consonants
# letter = input('Enter alphapets in lower case: ')
# if letter == 'a' or letter == 'e' or letter =='i' or letter =='o' or letter =='u':
#     print(letter, 'is a vowles')
# else:
#     print(letter, 'is a consonant') 

# Exam Result
maths = input('Enter the Maths Marks: ')
physics = input('Enter the Physics Marks: ')
chemistry = input('Enter the Chemistry Marks: ')
miniMumPassMark = 45
if int(maths) >= miniMumPassMark and int(physics) >= miniMumPassMark and int(chemistry) >= miniMumPassMark:
    print('Pass')
else:
    print('Fail')