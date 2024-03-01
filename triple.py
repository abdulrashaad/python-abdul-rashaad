

def append_q():


    cars = ['lambo', 'bmw', 'ferrari']

    print(cars)

    cars.append('corolla')

    print(cars)

if __name__ == '__main__':
    append_q()



def main():
    horror_books = ['Dracula', 'Carmilla', 'The Imago Sequence']

    print(horror_books.pop())
    print(horror_books)


if __name__ == '__main__':
    main()

def neew():
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    my_list.sort
    print(my_list)

    numbers = [100,12,43,4,5,78,32,24,56]
    numbers.sort(reverse=False)
    print(numbers)

    names = ['Rashard', 'Kamal', 'Aazakkkk', 'Baba']

    names.sort(key=len,reverse=False)
    print(names)


if __name__ == '__main__':
    neew()

def main():
    horror_books = ('Dracula', 'Carmilla', 'The Imago Sequence')

    print(horror_books)


if __name__ == '__main__':
    main()


def ranger():
    range_r = range(6, 11)
    print(range_r)

    a_range = list(range_r)
    print(a_range)
    a_range = tuple(range_r)
    print(a_range)

    for index in range(7):
        print(index)

if __name__ == '__main__':
    ranger()

def goss():

    family = ['Kamal', 'Baba', 'Fatima', 'Ammatullai', 'Yasmeen', 'Rashard', 'Amina', 'Razak', 'Laila']
    print(family[0])
    for index in range (len(family)):

        print(f'At index {index}, we have {family[index]}')
        print('Baba' in family)
if __name__ == '__main__':
        goss()



def main():
    random_numbers = [6, 1, 3, 8, 0, 9, 12, 3, 4, 0, 54, 8, 100, 55, 60, 70, 85]
    multiplied_random_numbers = []

    for number in random_numbers:
        multiplied_random_numbers.append(number * 2)

    print(multiplied_random_numbers)

if __name__ == '__main__':
    main()


def rant():
    rand_num = [4, 5, 7, 90, 32, 54, 12, 3, 1, 0, 18, 19, 22, 66]
    multiplied = []
    for kelz in rand_num:
        multiplied.append(kelz * 2)


    print(multiplied)


if __name__ == '__main__':
    rant()


def while_l():

    fast = 1
    while fast < 14:
        print(fast)
        fast += 1

if __name__ == '__main__':
    while_l()
def maiii():

    for x in range(3, 8):
        print()
        for y in range(1, 9):
            print(f'{x} x {y} = {x * y}')

if __name__ == '__main__':
    maiii()

def mainn():
    c = ['my brother', 'yussif', 'kelvin']
    d = ['your mother', 'yours', 'man']
    print(len(c))
    print(min(d))
    print(max(d))
    
    print(c + d * 3)
if __name__ == '__main__':
    mainn()




