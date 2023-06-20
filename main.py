from os import system as x
# pip install termcolor
from termcolor import colored
# pip install py-getch
import getch
import Sergey

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
    "Japan1": {
        "Information": "A blend of tradition and modernity with pleasant temperatures",
        "Climate": 1,
        "Price": 1,
        "Safety": 5
    },
    "Japan2": {
        "Information": "A blend of tradition and modernity with pleasant temperatures",
        "Climate": 2,
        "Price": 5,
        "Safety": 3
    },
    "Japan3": {
        "Information": "A blend of tradition and modernity with pleasant temperatures",
        "Climate": 2,
        "Price": 1,
        "Safety": 1
    },
    "Japan4": {
        "Information": "A blend of tradition and modernity with pleasant temperatures",
        "Climate": 5,
        "Price": 5,
        "Safety": 2
    },
    "Japan5": {
        "Information": "A blend of tradition and modernity with pleasant temperatures",
        "Climate": 2,
        "Price": 5,
        "Safety": 1
    },
    "Japan6": {
        "Information": "A blend of tradition and modernity with pleasant temperatures",
        "Climate": 2,
        "Price": 3,
        "Safety": 1
    },
    "Japan7": {
        "Information": "A blend of tradition and modernity with pleasant temperatures",
        "Climate": 1,
        "Price": 2,
        "Safety": 5
    },
    "Japan8": {
        "Information": "A blend of tradition and modernity with pleasant temperatures",
        "Climate": 2,
        "Price": 1,
        "Safety": 3
    },
    "Japan9": {
        "Information": "A blend of tradition and modernity with pleasant temperatures",
        "Climate": 3,
        "Price": 4,
        "Safety": 2
    },
    "Japan10": {
        "Information": "A blend of tradition and modernity with pleasant temperatures",
        "Climate": 5,
        "Price": 1,
        "Safety": 1
    }
    # Ill add the information for the other 22 countries here
}

def CreateAllDestinations(dict):
    return  list(dict.keys())

AllDestinations = CreateAllDestinations(database)

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
    if i==1 and j==2:
        input("Enter a countryname")
    elif i==1 and j==3:
        input("Here is a random country")
    elif i==2 and j==2:
        ListOfPref=Sergey.RunPromt()
        WeightedList=Sergey.AssignWeightedValues(ListOfPref,database)
        print(WeightedList)
        print(Sergey.OrderWeightedList(WeightedList))

        getch.getch()
    elif i==2 and j==3:
        input("Enter your preferences and get a surprise")
    elif i==3 and j==1:
        input("Enter a new country")
    



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
    if Move==" " and i==N:
        break
    if Move==" " and j>1:      #space executes command from submenu
        Execute(i,j)
        i=1
        j=1
    elif Move==" " and j==1:     #if submenu not empty space opens it, otherwise executes command
        if len(Sergey.TopLevel[i-1])>1:
            j=2
        else:
            Execute(i,j)
            i=1
            j=1
    Sergey.PrintMenu(i,j,N,W)
    if Move=="x":
        break

