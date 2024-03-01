def main():
    name = input('What is your name? ')
    print(f'Nice to meet you {name}')

    age = int(input(f'How old are you? {name}'))
    current_year = int(input(f'What is this year again? {name}'))
    hometown = input('Where are you from?')
    print(f'I am from {hometown}')
    sex = input('are a male or female?')
    print(f'i am a {sex}')





    print(f'If my calculations are right you wer born in the year: {current_year - age}')


if __name__ == '__main__':
    main()