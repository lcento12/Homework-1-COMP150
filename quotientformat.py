x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))
remainder = x%y
quotient = x//y
sentence = 'The quotient of {} and {} is {}, with a remainder of {}'.format(x,y,quotient,remainder)

print(sentence)
