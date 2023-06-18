## Structure of the code


+ Creates (optionally reads from file) the database. I am not completely sure what type of collection to use for it, dictionary seems a bad option. Probably a list of tuples?
+ Main menu. Top level options: Information, Choice of distination, Add a destination, Exit
    - Information.
        Calls a function that gets a list as an argument. The function prompts the user to type the first letters of his desired country and then shows all options from the list that fit the pattern. 
        +   If there is only one option: print the information about the country. 
        +  If more than one option: list the options and prompt again (I suggest type the already entered letters as part of the prompt and let the user print on, but not necessary).
        + No options: type something like Sorry, ma, wonna try again or go back to the menu.
        + As another possibility the user can choose to get to see a random destination. In that case the function from the choose destination block is called that shows a random destination from a list. The argument that is provided to the function in this case is the complete database. We should also decide whether this random option is called before the user is asked to enter a country (better option in my opinion), or if he just types "Random" to call it. 
        + Emtpy input (or some keyword) - go back to the menu. May be empty imput can also return the list of all available destinations. Let's see what works better.
    - Choice of destination. 
        +  Calls a function that asks the user for his preferences in different categories, one after another. The categories should be consistent with the structure of the database. Please make sure to communicate between those who work on those parts. An empty input in a category means irrelevant (legitimate input). Illigitimate inputs should be properly handeled and not cause the crush of the code.
            +  Optionally, in each category prompt for the importance of this category from 1 - not important to 5 - very important. Empty input on the previous step would then be not needed as it is equivalent to giving 1 as importance.
            +   If you decide to use the visualization of the type 1--------------X-----5 which is cool and not really difficult, talk to me. In any case I strongly suggest to use the getch module (run pip install py-getch; and then
            import getch) that allows to take a single keystroke without pressing enter. (Command getch.getch()) Thus you can for example describe what to do if the user pressed a number between 1 and 5 and then everything you did not explicitly describe just does nothing. Like this you have zero problems with handling illigitimate input.
            + Also optionally, at each step you can return to the previous step and make corrections.
        + After the list of preferences it formed, a function is called that takes the list of destinations and the preferences as arguments. With the algorithm you design the function returns a list of suggested destinations based on the provided criteria. Please talk to me about the algorithm if you need. Then the user is prompted whether he wants to see the list and choose himself, or whether he trusts the random, or whether he want to return to entering his preferences.
            - If he wants to see the list, the list is printed and the function from the information block is called, but this time not with the argument of the whole list, but the the argument being the list that has been just created. The user then, just in the information block starts to type the destination and when it is unambiguous, he is shown the information. Then he is asked whether to book (basically stop the program, as we are not going to booking, right?) or to return to the choice.  
            - If the user chooses random, he is shown a random destination from the list created previously. A function must be created that takes a list as an argument and prints a random destination from the list. In particular, if all preferences on the previous stage have been "irrelevent", the list coincides with the full database and a completely random destination is shown. Also here, may it is better let the user choose the option for random before he starts entering his preferences.
    - Adding a destination. Calls a function that asks the user to enter the destination, its description, and rate the destination according to all available criteria. An empty input in any of the categories is illigitimate! After that a new entry is addes to the database. If we decide to work with a file, so that the database changes do not disappear each time the program is restarted, then the new entry must be added to the file as well.
    -  Exit. Well. Exit.
+ Only the main menu (and possibily the creation of the database) is in the master file. All other functions are described in separate modules and added after they are tested.
   - When you work on a function that is supposed to return something (and not just print the result), keep attention to where this returned value is used and make sure the formats match between different places where the same object is used. That means, communicate horizontally. I do not prescribe the format of each object, just saying what functions should do. it is up to you to make sure different parts of the code fit to each other.
   - Functions should be done by Wednesday evening and pushed to you branches. On Thursday we bring them together.
     

              