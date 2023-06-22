"""In my modified code where we are using a list as the argument and so we can directly access the elements of the sublist using indexing."""
import random

def random_value(variable):
    if isinstance(variable, int):
        return random.randint(1, variable)
    elif isinstance(variable, float):
        return random.uniform(0, variable)
    elif isinstance(variable, str):
        return random.choice(variable)
    elif isinstance(variable, list):
        destination = random.choice(variable)
        country_name = destination[0]
        country_info = destination[1]
        country_data = ',\n'.join(destination[2:])
        return f"We do suggest you to take a look at data of: {country_name}\n{country_info}\n{country_data}"
    else:
        return None  # Handle unsupported variable types

database = [
    ["Germany", "Rich history, vibrant cities, and a cool climate", "Climate: 2", "Price: 3", "Safety: 4"],
    ["Japan", "A blend of tradition and modernity with pleasant temperatures", "Climate: 4", "Price: 3", "Safety: 4"],
    ["Australia", "Stunning landscapes, diverse wildlife, and a sunny climate: 5", "Price: 5", "Safety: 5"],

    
]

random_result = random_value(database)
print(random_result)
