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
        #country_name = destination[0]
        #country_info = destination[1]
        #country_data = ',\n'.join(destination[2:])
        #return (Sergey.ShowCountryInfo)
        return destination
    else:
        return None  # Handle unsupported variable types
