def main():
    num = int(input('what numer would you like to check?\n'))
    is_not_prime = False

    if num == 1:
        print(f'{num} is not a prime number.')
    elif num > 1:
        for n in range(2,num):
            if (num % n) == 0:
                is_not_prime = True
                print(f'{num} is not a prime number..')
                break
        else:
         print(f'{num} is a prime number.')

if __name__ == '__main__':
        main()

def main():
    str = 'i have stopped any thing that will distract me'
    print(str.split())
if __name__ == '__main__':
        main()

def main():
    age = int(input('what is your age?\n'))
    if(age < 22 ):
        print(f'{age} is not correct')
    elif(age % 2 == 0):
        print(f'{age} is considerable')
if __name__ == '__main__':
    main()