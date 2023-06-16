# Travel destination

- The user is promped whether he want to look up a particular country or look for a suitable travel destination

- Information block:
   + if he wants to get information he is offered a list of available countries (optional he enters the first letter of the country and then the countries that start with that sequence are shown, probably better from the point of view of representablity)
   + Chooses the country (optional if there is only one country starting with the proposed string it is the choice) - then he is shown the information about the country stored in the dictionary. (Climate, location, big cities, how expensive it is probably other categories.)

- Looking for destination block:
   + The user is asked to input differnt types of climate, price range and may be other features from available lists. If a certain category is irrelevant just empty input.
   + After that a list is formed based on the provided criteria.
   + Then the user is asked whether he wants to get more information on a country from the list, if yes, return to information block.

- We need a database of countries (cities, travel destinations?) with all attributes (climate, location, price range etc.) And a way to work with such a database looking through it and picking entries that fit specific criteria. 
   