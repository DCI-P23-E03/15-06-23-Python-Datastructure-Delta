import random

country_names = {
    "Germany": {},
    "Japan": {},
    
    #name of 22 other countries will be shown here
}


database = {
    "Germany": {
        "Information": "Rich history, vibrant cities, and a cool climate",
        "Climate": 2,
        "Price": 3,
        "Safety": 4
    },
    "Japan": {
        "Information": "A blend of tradition and modernity with pleasant temperatures",
        "Climate": 4,
        "Price": 3,
        "Safety": 4
    }
    # Ill add the information for the other 22 countries here
}

def CreateAllDestinations():
    return  list(database.keys())

#def ShowRandom(lst):
    #random_country = random.choice(lst)
    #print("Our suggestion is", random_country)
    #PrintCountryInfo(random_country)

def PrintCountryInfo(country):
    info = database[country]["Information"]
    climate = database[country]["Climate"]
    price = database[country]["Price"]
    safety = database[country]["Safety"]

    print("Country:", country)
    print("Information:", info)
    print("Climate:", climate)
    print("Price:", price)
    print("Safety:", safety)

# Code execution after "Show random country" option is chosen
AllDestinations = CreateAllDestinations()
#ShowRandom(AllDestinations)
print(AllDestinations)
