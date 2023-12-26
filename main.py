def main():
    print('Hello, World!')


if __name__ == '__main__':
    main()

def carlo():
    book, author, release_year, rating = 'love_rocks', 'rashard', 1999, 4.122

    print(f'{book} is a novel by {author}, published in {release_year}.' 
          f'It has a rating of {rating} on good reads')



if __name__ == '__main__':
    carlo()

def numbers():
    num_1 = 60
    num_2 = 20

    print(f'the sum of num_1 and num_2 is: {num_1 + num_2}')
    print(f'the difference of num_1 and num_2 is: {num_1 - num_2}')

if __name__ == '__main__':
    numbers()

from library2 import dec

def main():
    dec()
    x = 15
    y = 12

    print(f'the sum of the decimal numbers is: {x + y}')
    print(f'the product of the decimal numbers is: {x * y}')
    print(f'the quotient of x and y is: {x/y}')
    print(f'the quotient of y and x is = {y/x}')
    print(f'the quotient of y and x = {y//x}')
    print(f'the remainder of x and y = {x%y}')
if __name__ == '__main__':
    main()


def main():
    float_variable = 9.25
    integer_variable = 55
    absolute_variable = -33


    print(f'{float_variable} converted to an integer is: {int(float_variable)}')
    print(f'{integer_variable} converted to a float is: {float(integer_variable)}')
    print(f'{absolute_variable} converted is: {abs(absolute_variable)}')


if __name__ == '__main__':
    main()

def power():

    a = 2
    b = 3

    print(f'{2} to the power of {3} is: {pow(2, 3)}')
    print(f'{a} to the power {b} = {a ** b}')


if __name__ == '__main__':
    power()

def divisionmod():

    f = 5
    j = 2

    print(f'division and modulos of {f} and {j} = {divmod(f, j)}')

if __name__ == '__main__':
    divisionmod()








