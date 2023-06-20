# Travel destination

- The user is promped whether he want to look up a particular country or look for a suitable travel destination

- Information block:
   + if he wants to get information he is offered a list of available countries (optional he enters the first letter of the country and then the countries that start with that sequence are shown, probably better from the point of view of usability)
   + Chooses the country (optional if there is only one country starting with the proposed string it is the choice) - then he is shown the information about the country stored in the dictionary. (Climate, location, big cities, how expensive it is probably other categories.)

- Looking for destination block:

   + The user is asked to input different types of climate, price range and may be other features from available lists. If a certain category is irrelevant just empty input. For example the user is asked which climate he prefers and he enters a number from 1 (coldest) to 5(hottest). 0 for doesn't matter. (optional: go back and change previous input option.)
   (very optional: user can enter how important is that particular criterium for him. That is done by inputing number between 1 and 5. Very very optional: visualisation of the weight with something like:
   1--------------X-----5)
   + After that a list is formed based on the provided criteria. A reasonable algorithm for determining the list must be developed. please provide a description of the proposed algorithm separately.
   + After the list is formed, the user is asked whether he wants a random country (destination) from the list or if he wants to see the list and choose himself. 
   + If the first option, the user get a random country from the list with its description
   + If the second option is chosen, the user is shown the list (should be of at least 2 at most 5 countries, in case the algorithm can not determine 5 best countries, as there is equality between many countries based on the available criteria, for example if the user just enters no criteria at all, then a random pool of 5 countries from the best ones available is shown). After that he chooses a destination from the list in the same manner as is done in the information block.

- The user should also be able to add a travel destination providing its description. (Optional: the database is stored in a separate file so that the added information is not lost after the program is closed and restarted.)

- We need a database of countries (cities, travel destinations?) with all attributes (climate, location, price range etc.) And a way to work with such a database looking through it and picking entries that fit specific criteria. 
   