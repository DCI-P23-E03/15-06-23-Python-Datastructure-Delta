import getch
from os import system as x
from termcolor import colored





def DrawSkala(i,bool):   # Draws a scale menu of the type <......X..........>
    SkalaRange=5
    Skala=""
    Skala+="<"+(i-1)*"....."+"..X.."+(SkalaRange-i)*"....."+">"
    if bool:
        Skala+=colored("  █",'red')    #Puts a mark at the currently active menu
    return Skala

def PrintField(Cur,Preferences,Importance):    # Prints all six scale menus
    x("clear")
    print("Use s, w to navigate; a, d to change the input, space to submit.\n\n")
    print("Prefered climate (1 coldest, 5 hottest):\n"+DrawSkala(Preferences[0],Cur==0)+"\n   1    2    3    4    5\n")
    print("Imortance of climate (1 unimportant, 5 very important):\n"+DrawSkala(Importance[0],Cur==1)+"\n   1    2    3    4    5\n")
    print("Prefered price range (1 cheapest, 5 most expensive):\n"+DrawSkala(Preferences[1],Cur==2)+"\n   1    2    3    4    5\n")
    print("Imortance of price (1 unimportant, 5 very important):\n"+DrawSkala(Importance[1],Cur==3)+"\n   1    2    3    4    5\n")
    print("Prefered safety (1 war zone, 5 safest):\n"+DrawSkala(Preferences[2],Cur==4)+"\n   1    2    3    4    5\n")
    print("Imortance of safety (1 unimportant, 5 very important):\n"+DrawSkala(Importance[2],Cur==5)+"\n   1    2    3    4    5\n")

def RunPromt():     # User changes his preferences
    Preferences=[3,3,3]
    Importance=[1,1,1]  
    Cur=0
    while True:
        PrintField(Cur,Preferences,Importance)
        Move=getch.getch()
        if Move=="w" and Cur>0:   # Navigating the menus
            Cur-=1
        if Move=="s" and Cur<5:
            Cur+=1
        if Move=="a" and Cur%2==0 and Preferences[Cur//2]>1:    # Changing the value at the current menu
            Preferences[Cur//2]-=1
        if Move=="a" and Cur%2==1 and Importance[Cur//2]>1:
            Importance[Cur//2]-=1
        if Move=="d" and Cur%2==0 and Preferences[Cur//2]<5:
            Preferences[Cur//2]+=1
        if Move=="d" and Cur%2==1 and Importance[Cur//2]<5:
            Importance[Cur//2]+=1
        if Move==" ":    # Select and return chosen values
            break

    return [Preferences,Importance]

def AssignWeightedValues(ListOfPref, database):    # Calculates the absolute value of the discrepancy from the desired value of a parameter and the value of that parameter for a given destination. Multiplies the result with the user-selected importance (importance 1 means multiplication by 0)
    WeightedList=[]
    InfoKeys=["Climate","Price","Safety"]
    for x in database:
        Discrepancy=0
        for y in InfoKeys:
            Discrepancy+=abs(ListOfPref[0][InfoKeys.index(y)]-database[x][y])*(ListOfPref[1][InfoKeys.index(y)]-1)
        WeightedList.append([x,Discrepancy])
    return WeightedList   

def ReturnWeight(item):
    return item[1]

def OrderWeightedList(WeightedList):   #Sorts the destination according to AssignedWeightedValues
    WeightedList.sort(key=ReturnWeight)
    Chop=3
    while WeightedList[Chop-1][1]==WeightedList[Chop][1]:    #If there's a tie between 3rd and 4th place includes all places after the 3rd one that are tied
        Chop+=1
        if Chop==len(WeightedList):
            break
    WeightedListStrippedChopped=[]
    for i in range(Chop):
        WeightedListStrippedChopped.append(WeightedList[i][0])
    return WeightedListStrippedChopped

TopLevel = [[["Info","i"],"Input","Random"],[["Choose","c"],"Input","Random"],[["apPend","p"]],[["eXit","x"]]] # Last item must be Exit

def TopMenu(i,N,W):
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

def TopMenuBottomOpen(i,N,W):
    if i==1:
        bottomOpen="├"+"─"*W+"┼"+"─"*W+("┴"+"─"*W)*(N-2)+"┘\n"
    elif i==N:
        bottomOpen="└"+"─"*W+("┴"+"─"*W)*(N-2)+"┼"+"─"*W+"┤\n"
    else:
        bottomOpen="└"+"─"*W+("┴"+"─"*W)*(i-2)+"┼"+"─"*W+"┼"+("─"*W+"┴")*(N-i-1)+"─"*W+"┘\n"
    return bottomOpen      #  bottom of menu open at i-th position


def DropOutMenuOpen(i,j,W):    #Dropout menu at i-th horizontal position highlighted at j-th vertical position
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

def PrintMenu(i,j,N,W):     #prints the menu 
    top="┌"+"─"*W+("┬"+"─"*W)*(N-2)+"┬"+"─"*W+"┐\n"  # top of menu
    bottom="└"+"─"*W+("┴"+"─"*W)*(N-1)+"┘\n"      # bottom of closed menu
    middle = TopMenu(i,N,W)
    x("clear")
    print("a,s,d,w or shortcuts to navigate, space to select")
    if j==1:    # closed menu
        print(top+middle+bottom)
    else:       # menu open at i-th position
        bottomOpen=TopMenuBottomOpen(i,N,W)
        DropOutMenu=DropOutMenuOpen(i,j,W)
        print(top+middle+bottomOpen+DropOutMenu)

def ReadDatabase(): # reads dictionary from database.txt
    x("chmod 664 database.txt")
    with open("database.txt","at"):
        pass
    database={}
    with open("database.txt") as f:
        string=f.read().replace("\t","").splitlines()
        print(len(string))
        for i in range(0,len(string),6):
            #print(i)
            database[string[i].title()]={"Information":string[i+1],"Climate":int(string[i+2]),"Price":int(string[i+3]),"Safety":int(string[i+4])}
        #print(database)
    x("chmod 444 database.txt")
    return database

def WriteDatabase(database):   # writes dictionary database to database.txt
    x("chmod 664 database.txt")
    with open("database.txt","wt") as f:
        string=""
        for i,j in database.items():
            
            string+=i+"\n\t"
            for k in j.values():
                string+=str(k)+"\n\t"
            string+="\n" 
        f.write(string)
    x("chmod 444 database.txt")
        
def ShowCountryInfo(country,database):  # types info about (country) from (database). Numerical values for Prices and Safety are replaced with fixed short phrases
    print("""
    Travel Destination Recommendation System\n
    Here, we want to make sure we recommend the best countries for you to travel.
    """)
    Prices=["Extremely affordable!", "Quite affordable!", "Reasonable prices!", "High-level location!", "Luxury travel!"]
    Safety=["For those who enjoy danger!", "For risk-lovers!", "For those keeping their cool!", "Relaxed travel!", "Everything is taken care of!"]
    if country in database:
        print("Our recomendation is: "+country+ '\n'+ database[country]['Information']+"\n"+Prices[database[country]["Price"]-1]+"\n"+Safety[database[country]["Safety"]-1])
    if country not in database:
        print(f"We are sorry, {country} is not in our database")

def AppendDatabase(database): #Adds an entry to the database. Pretty self-explainatory
    x("clear")
    CurStr=""
    country=input("Enter a new country to add to our database (enter q at any moment to quit): ").title()
    if country in database:
        print("We already have this one.")
    elif country.upper()=="Q":
        return None
    else: 
        CurStr+=f"Enter a new country to add to our database (enter q at any moment to quit): {country}\n"
        
        flag=0
        while True:
            x("clear")
            if flag==0:
                print(CurStr)
                print(f"Rate the climate of {country} from 1 coldest to 5 hottest: ")
            else:
                x("clear")
                print(CurStr)
                #Highlights red if entry not a digit from 1 to 5
                print(f"Rate the climate of {country} "+colored("from 1 coldest to 5 hottest: ","red"))
            Climate=getch.getch()
            if Climate.upper()=="Q":    #stops appending
                return None
            if not Climate.isnumeric():
                flag=1
            elif int(Climate)<1 or int(Climate)>5:
                flag=1
            else:
                flag=0
                CurStr+=f"Rate the climate of {country} from 1 coldest to 5 hottest: "+Climate+"\n"
                break
        
        while True:
            x("clear")
            if flag==0:
                print(CurStr)
                print(f"Rate the prices in {country} from 1 cheapest to 5 most expensive: ")
            else:
                x("clear")
                print(CurStr)
                print(f"Rate the prices of {country} "+colored("from 1 cheapest to 5 most expensive: ","red"))
            Prices=getch.getch()
            if Prices.upper()=="Q":
                return None
            if not Prices.isnumeric():
                flag=1
            elif int(Prices)<1 or int(Prices)>5:
                flag=1
            else:
                flag=0
                CurStr+=f"Rate the prices in {country} from 1 cheapest to 5 most expensive: "+Prices+"\n"
                break

        while True:
            x("clear")
            if flag==0:
                print(CurStr)
                print(f"Rate the safety in {country} from 1 war zone to 5 safest: ")
            else:
                x("clear")
                print(CurStr)
                print(f"Rate the safety of {country} "+colored("from 1 war zone to 5 safest: ","red"))
            Safety=getch.getch()
            if Safety.upper()=="Q":
                return None
            if not Safety.isnumeric():
                flag=1
            elif int(Safety)<1 or int(Safety)>5:
                flag=1
            else:
                flag=0
                CurStr+=f"Rate the prices in {country} from 1 war zone to 5 safest: "+Safety+"\n"
                break
        
        x("clear")
        print(CurStr)
        #print("\n")
        Info=input(f"Write a few words about {country}: ")
        if Info.upper()=="Q":
            return None
        print("\nThank you for your input. We added it to our database.")
        database.update({
            country:{
                "Information":Info,
                "Climate":int(Climate),
                "Price":int(Prices),
                "Safety":int(Safety)
                    }
                })

def CreateAllDestinations(dicta):
    #dicta=ReadDatabase()
    return  list(dicta.keys())
    """
    ListDist=[]
    for key in dicta:
        ListDist.append(key)
    return ListDist
    """

    