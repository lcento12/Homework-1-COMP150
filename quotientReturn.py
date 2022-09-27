def quotientString(x, y):
    remainder = x%y
    quotient = x//y
    return 'The quotient of {} and {} is {}, with a remainder of {}'.format(x,y,quotient,remainder)

def main():
    print(quotientString(3038380, 293892))
    print(quotientString(200, 80))
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    print(quotientString(a, b))

main()

