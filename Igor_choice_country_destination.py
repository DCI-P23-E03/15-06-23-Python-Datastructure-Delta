#new version
import os
import platform
from getch import getch


def clear_screen():
    current_os = platform.system()
    if current_os == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def search_country(countries):
    clear_screen()
    print("Please type a distination country :")

    while True:
        letter = getch()  # Input of ch
        print(letter)

        
        matching_countries = [
            country for country in countries if country.startswith(letter)
        ]

        if not matching_countries:
            clear_screen()
            print(f"Sorry, there is not country starting with {letter}, try again")
            continue

        while len(matching_countries) > 1:
            print(f'Please find a country in list of available destination {matching_countries} and continue to type \n {letter}')
            letter_2 = getch()
            letter += letter_2
            print(letter)

            clear_screen()

            for i, country in enumerate(matching_countries, start=1):
                print()
                #print(f"{country}",': Is this country?')

            matching_countries = [
                country for country in matching_countries if country.startswith(letter)
            ]
            print(matching_countries)

        return matching_countries[0]


travel_countries = ['France', 'Filippinen', 'Fiji', 'Fuji',
                    'Italy', 'Spain', 'Thailand', 'FFff', 'Japan', 'Australia']

country_choice = search_country(travel_countries)
if country_choice:
    print(f"Your choice : {country_choice}")
