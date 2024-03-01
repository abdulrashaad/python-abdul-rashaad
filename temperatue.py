def main():
    temperature_in_celsius = input(f'What is the temperature in celsius? ')

    temperature_in_fahrenheit = (float(temperature_in_celsius) * 1.8) + 32

    print(f'{temperature_in_celsius} degree celsius is equivalent to {temperature_in_fahrenheit} degree fahrenheit.')


if __name__ == '__main__':
    main()