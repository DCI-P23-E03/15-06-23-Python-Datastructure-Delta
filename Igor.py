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
    #clear_screen()   
    CurStr="Please start typing your country of interest: "
    print(CurStr)
    letter = getch().upper()  # Input of ch
    while True:
        clear_screen()       
        print(CurStr)
        print(letter)
        matching_countries = [
                country for country in countries if country.lower().startswith(letter.lower())
                            ]
        if not matching_countries:
            print(f"Sorry, there is no country starting with {letter}, enter another one")
            letter = getch().upper() 
            continue
        for country in matching_countries:
            print(country)
        CurStr+="\n"+letter
        break

    while len(matching_countries) > 1:
            #print(f'Please find a country in list of available destination {matching_countries} and continue to type \n {letter}')
        letter_2 = getch()
        letter+=letter_2
        CurStr += letter_2
        clear_screen()
        print(CurStr)
        flag=True
            #matching_countries = [country for country in matching_countries if country.startswith(letter)]
        for country in matching_countries:
            if country.lower().startswith(letter.lower()):
                print(country)
                flag=False
            
           



        if flag:
            for country in matching_countries:
                print(country)
            print(f"Sorry, there is no country starting with {letter}, change the last letter")
            letter=letter[:-1]
            CurStr=CurStr[:-1]
                
            continue

        matching_countries = [
            country for country in matching_countries if country.lower().startswith(letter.lower())
                                 ]  
            
    return matching_countries[0]

"""
travel_countries = ['France', 'Filippinen', 'Fiji', 'Fuji',
                    'Italy', 'Spain', 'Thailand', 'FFff', 'Japan', 'Australia', 'United States', 'United Kingdom']

country_choice = search_country(travel_countries)
if country_choice:
    print(f"Your choice : {country_choice}")
"""