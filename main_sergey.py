from os import system as x
# pip install termcolor
from termcolor import colored
# pip install py-getch
import getch
import Sergey
import random
import Random_Function
import Igor

"""
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
    },
    "Australia": {
        "Information": "Stunning landscapes, diverse wildlife, and a sunny climate",
        "Climate": 5,
        "Price": 5,
        "Safety": 5
    },
    "Canada": {
        "Information": "Breathtaking nature, friendly locals, and a cold climate",
        "Climate": 2,
        "Price": 4,
        "Safety": 4
    },
    "Italy": {
        "Information": "Art, culture, and delicious cuisine with a cold climate",
        "Climate": 2,
        "Price": 3,
        "Safety": 3
    },
    "Brazil": {
        "Information": "Beautiful beaches, vibrant festivals, and a hot climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 3
    },
    "Thailand": {
        "Information": "Exotic temples, stunning islands, and a hot climate",
        "Climate": 4,
        "Price": 2,
        "Safety": 3
    },
    "South Africa": {
        "Information": "Safari adventures, diverse landscapes, and a hot climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 3
    },
    "United States": {
        "Information": "Iconic cities, natural wonders, and a cold climate",
        "Climate": 2,
        "Price": 4,
        "Safety": 4
    },
    "France": {
        "Information": "Romantic atmosphere, world-class cuisine, and a cold climate",
        "Climate": 2,
        "Price": 3,
        "Safety": 4
    },
    "China": {
        "Information": "Great Wall, ancient history, and a cold climate",
        "Climate": 2,
        "Price": 3,
        "Safety": 3
    },
    "India": {
        "Information": "Rich culture, diverse traditions, and a hot climate",
        "Climate": 5,
        "Price": 1,
        "Safety": 2
    },
    "Egypt": {
        "Information": "Ancient pyramids, Nile River, and a hot climate",
        "Climate": 5,
        "Price": 2,
        "Safety": 3
    },
    "Mexico": {
        "Information": "Colorful culture, stunning beaches, and a hot climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 3
    },
    "Russia": {
        "Information": "Vast landscapes, rich history, and a cold climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 3
    },
    "United Kingdom": {
        "Information": "Historic landmarks, charming villages, and a cold climate",
        "Climate": 2,
        "Price": 3,
        "Safety": 4
    },
    "Greece": {
        "Information": "Mythology, picturesque islands, and a hot climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 3
    },
    "Turkey": {
        "Information": "Cultural heritage, stunning coastlines, and a hot climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 3
    },
    "Argentina": {
        "Information": "Tango, Patagonia, and a varied climate",
        "Climate": 3,
        "Price": 3,
        "Safety": 3
    },
    "New Zealand": {
        "Information": "Adventure sports, breathtaking landscapes, and a moderate climate",
        "Climate": 3,
        "Price": 4,
        "Safety": 4
    },
    "Malaysia": {
        "Information": "Rainforests, stunning beaches, and a hot climate",
        "Climate": 4,
        "Price": 2,
        "Safety": 3
    },
    "Sweden": {
        "Information": "Scenic beauty, cultural heritage, and a cold climate",
        "Climate": 3,
        "Price": 3,
        "Safety": 4
    },
    "Spain": {
        "Information": "Vibrant festivals, beautiful beaches, and a hot climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 4
    },
    "South Korea": {
        "Information": "K-pop, traditional palaces, and a moderate climate",
        "Climate": 3,
        "Price": 3,
        "Safety": 4
    },
    "Seychelles": {
        "Information": "Idyllic beaches, turquoise waters, and diverse marine life",
        "Climate": 5,
        "Price": 4,
        "Safety": 4
    }
}
"""

database=Sergey.ReadDatabase()

"""
def CreateAllDestinations(dicta):
    #return  list(dicta.keys())
    ListDist=[]
    for key in dicta:
        ListDist.append(key)
    return ListDist
"""

AllDestinations = Sergey.CreateAllDestinations(database)




N=4 # number of menu items
W=8 # width of menu item
#TopLevel = [[["Info","i"],"Input","Random"],[["Choose","c"],"Input","Random"],[["apPend","p"]],[["eXit","x"]]]

ShortCut=[]
p=0
while p<len(Sergey.TopLevel):    # creates a list of keyboard shortcuts
    ShortCut.append(Sergey.TopLevel[p][0][1])
    p+=1

# Elements of the menu
"""
top="┌"+"─"*W+("┬"+"─"*W)*(N-2)+"┬"+"─"*W+"┐\n"  # top of menu
bottom="└"+"─"*W+("┴"+"─"*W)*(N-1)+"┘\n"      # bottom of closed menu


def TopMenu(i):
    k=1
    middle=""
    while k<=N:
        if k!=i:
           middle+="│"+TopLevel[k-1][0][0].center(W)
        else: 
           middle+="│"
           middle+=colored(TopLevel[k-1][0][0].center(W),'green') 
        k+=1
    middle+="│\n" 
    return middle    #  highlighted top menu item

def TopMenuBottomOpen(i):
    if i==1:
        bottomOpen="├"+"─"*W+"┼"+"─"*W+("┴"+"─"*W)*(N-2)+"┘\n"
    elif i==N:
        bottomOpen="└"+"─"*W+("┴"+"─"*W)*(N-2)+"┼"+"─"*W+"┤\n"
    else:
        bottomOpen="└"+"─"*W+("┴"+"─"*W)*(i-2)+"┼"+"─"*W+"┼"+("─"*W+"┴")*(N-i-1)+"─"*W+"┘\n"
    return bottomOpen      #  bottom of menu open at i-th position


def DropOutMenuOpen(i,j):
    DropOutMenu=""
    k=1
    while k<len(TopLevel[i-1]):
        if j==k+1:
            DropOutMenu+=" "*(W+1)*(i-1)+"│"+colored(TopLevel[i-1][k].center(W),'blue')+"│\n"
        else:
            DropOutMenu+=" "*(W+1)*(i-1)+"│"+TopLevel[i-1][k].center(W)+"│\n"
        k+=1
    DropOutMenu+=" "*(W+1)*(i-1)+"└"+"─"*W+"┘\n"
    return DropOutMenu


def PrintMenu(i,j):
    middle = TopMenu(i)
    x("clear")
    print("a,s,d,w or shortcuts to navigate, space to select")
    if j==1:    # closed menu
        print(top+middle+bottom)
    else:       # menu open at i-th position
        bottomOpen=TopMenuBottomOpen(i)
        DropOutMenu=DropOutMenuOpen(i,j)
        print(top+middle+bottomOpen+DropOutMenu)
"""
def Execute(i,j):
    global AllDestinations
    if i==1 and j==2:
        choice=Igor.search_country(AllDestinations)
        print(f"\nYour choice is {choice}.")
        Sergey.ShowCountryInfo(choice, database)
        print("\nPress any key to return to menu, x to quit.")
        Mov=getch.getch()
        return Mov
    elif i==1 and j==3:
        
        #AllDestinations = Sergey.CreateAllDestinations()
        Sergey.ShowCountryInfo(Random_Function.random_value(AllDestinations), database)
        print("\nPress any key to return to menu, x to quit.")
        Mov=getch.getch()
        return Mov
    elif i==2 and j==2:
        ListOfPref=Sergey.RunPromt()
        WeightedList=Sergey.AssignWeightedValues(ListOfPref,database)
        OrderderWeightedList=Sergey.OrderWeightedList(WeightedList)
        string="According to our esperts the best options for you are: "
        for i,country in enumerate(OrderderWeightedList):
        
            string+=country
            if i<len(WeightedList)-1:
                string+=", "
            else:
                string+="."
        string+="\nStart typing the country you want to see."
        print(string)
        
        #print(WeightedList)
        choice=Igor.search_country(OrderderWeightedList)
        #print(Sergey.OrderWeightedList(WeightedList))
        #print("Now you choose one country out of that options with Igor's block and get information about that country with Gloria's block")
        #Sergey.ShowCountryInfo(Sergey.OrderWeightedList(WeightedList)[0], database)
        print(f"\nYour choice is {choice}.")
        Sergey.ShowCountryInfo(choice, database)
        print("\nPress any key to return to menu, x to quit.")
        Mov=getch.getch()
        return Mov
    elif i==2 and j==3:
        ListOfPref=Sergey.RunPromt()
        WeightedList=Sergey.AssignWeightedValues(ListOfPref,database)
        #print(WeightedList)
        #print(Sergey.OrderWeightedList(WeightedList))
        #print("Now you get a random country out of this list with Sam's block and get information about that country with Gloria's block")
        Sergey.ShowCountryInfo(Random_Function.random_value(Sergey.OrderWeightedList(WeightedList)), database)
        print("\nPress any key to return to menu, x to quit.")
        Mov=getch.getch()
        return Mov
    elif i==3 and j==1:
        Sergey.AppendDatabase(database)
        AllDestinations = Sergey.CreateAllDestinations(database)
        #print(database)
        Sergey.WriteDatabase(database)
        print("\nPress any key to return to menu, x to quit.")
        Mov=getch.getch()
        return Mov


i=1
j=1
x("clear")
Sergey.PrintMenu(i,j,N,W)
while True:
    Move=getch.getch().lower()
    if Move=="a":
        if i>1:
            i-=1
            if j>len(Sergey.TopLevel[i-1]):   #checks the size of the dropout menu at the new position. If too large - adjust.
                j=len(Sergey.TopLevel[i-1])
    if Move=="d":
        if i<N:
            i+=1
            if j>len(Sergey.TopLevel[i-1]):
                j=len(Sergey.TopLevel[i-1])
    if Move=="s":
        if j<len(Sergey.TopLevel[i-1]):
           j+=1
    if Move=="w":
        if j>1:
           j-=1
    if Move in ShortCut:     # if shortcut is used, moves to the corresponding menu item and opens menu
        i=ShortCut.index(Move)+1
        if len(Sergey.TopLevel[i-1])>1:
            j=2
        else:
            j=1
    if Move==" " and i==N:    #Exit menu item is assumed to be on the last spot.
        break
    if Move==" " and j>1:      #space executes command from submenu
        Move=Execute(i,j)
        i=1
        j=1
    elif Move==" " and j==1:     #if submenu not empty space opens it, otherwise executes command
        if len(Sergey.TopLevel[i-1])>1:
            j=2
        else:
            Move=Execute(i,j)
            i=1
            j=1
    Sergey.PrintMenu(i,j,N,W)
    if Move=="x":
        break

