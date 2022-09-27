def createDictionary():
    number = dict()
    number['one'] = 1
    number['two'] = 2
    number['three'] = 3
    number['four'] = 4
    return number

def main():
    dictionary = createDictionary()
    print(dictionary['one'])
    print(dictionary['two'])
    print(dictionary['three'])
    print(dictionary['four'])

main()
