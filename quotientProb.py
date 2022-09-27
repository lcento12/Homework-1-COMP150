def quotientProb(x, y):
    remainder = x%y
    quotient = x//y
    sentence = 'The quotient of {} and {} is {}, with a remainder of {}'.format(x,y,quotient,remainder)
    print(sentence)

def main():
    quotientProb(3038380, 293892)
    quotientProb(200, 80)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    quotientProb(a, b)

main()

