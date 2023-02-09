def main():
    print('This program converts US dollars to Taka')
    print()

    dollars = eval(input('Enter amount in dollars: '))

    Taka = convert_to_taka(dollars)

    print('This is ', Taka, 'taka')


convert_to_taka = lambda dollars: dollars * 97

main()