from string import capwords


def main():
    mum_name = 'ayisha'
    print(len(mum_name))
    print(mum_name.capitalize())


if __name__ == '__main__':
    main()

def rest():

    clean = '''i want's to rest'''
    print(capwords(clean))


if __name__ == '__main__':
    rest()


def main():
    book_name = "alice's adventures in wonderland"

    print(capwords(book_name))


if __name__ == '__main__':
    main()

def main():
    item = 'sex toy boy'
    print(f'{item} is converted to',item.swapcase())
if __name__ == '__main__':
    main()

def main():
    ghana = 'kudus'
    print(ghana)
    print(f'is {ghana} in upper case?',{ghana.isupper()})
    print(f'is {ghana} in lower case?',{ghana.islower()})
if __name__ == '__main__':
    main()

def main():
    paragraph = '''At three in the morning the chief Sussex detective, obeying the urgent call from Sergeant Wilson of 
    Birlstone, arrived from headquarters in a light dog-cart behind a breathless trotter. By the five-forty train in 
    the morning he had sent his message to Scotland Yard, and he was at the Birlstone station at twelve o'clock to 
    welcome us. White Mason was a quiet, comfortable-looking person in a loose tweed suit, with a clean-shaved, 
    ruddy face, a stoutish body, and powerful bandy legs adorned with gaiters, looking like a small farmer, 
    a retired gamekeeper, or anything upon earth except a very favourable specimen of the provincial criminal 
    officer.'''

    substring = 'the'

    print(f'The substring "{substring}" shows up {paragraph.count(substring)} times in the paragraph.')


if __name__ == '__main__':
    main()

def main():
    motive = 'I will travel to Italy verysoon Insha Allah'
    print(motive)
    motive = motive.split(',',5)
    print(motive)
if __name__ == '__main__':
    main()


def main():
    number = int(input('what number would you like to check?\n'))
    if number % 10 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is found odd.")
if __name__ == '__main__':
    main()

def main():
    days = int(input('how long does it take receive nulla osta?\n '))
    if days % 100 == 0 and days % 21 == 0:
        print(f"{days} is 90 days.")
    elif days % 20 == days % 10 == 0:
        print(f"{days} is 90 days correct.")
    else:
        print(f"{days} is not 90 days.")
if __name__ == '__main__':
    main()

def main():
    num = int(input('what numer would you like to check?\n'))
    is_not_prime = False

    if num == 1:
        print(f'{num} is not a prime number.')
    elif num > 1:
        for n in range(2,num):
            if (num % n) == 0:
                is_not_prime = True
                break
    else:
        print(f'{num} is a prime number')

if __name__ == '__main__':
        main()
