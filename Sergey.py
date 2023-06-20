import getch
from os import system as x
from termcolor import colored



SkalaRange=5
Preferences=[1,1,1]
Importance=[1,1,1]  
Cur=0

def DrawSkala(i,bool):
    Skala=""
    Skala+="<"+(i-1)*"....."+"..X.."+(SkalaRange-i)*"....."+">"
    if bool:
        Skala+=colored("  █",'red')
    return Skala

def PrintField(Cur):
    x("clear")
    print("Use s, w to navigate; a, d to change the input, space to submit.\n\n")
    print("Prefered climate (1 coldest, 5 hottest):\n"+DrawSkala(Preferences[0],Cur==0)+"\n   1    2    3    4    5\n")
    print("Imortance of climate (1 unimportant, 5 very important):\n"+DrawSkala(Importance[0],Cur==1)+"\n   1    2    3    4    5\n")
    print("Prefered price range (1 cheapest, 5 most expensive):\n"+DrawSkala(Preferences[1],Cur==2)+"\n   1    2    3    4    5\n")
    print("Imortance of price (1 unimportant, 5 very important):\n"+DrawSkala(Importance[1],Cur==3)+"\n   1    2    3    4    5\n")
    print("Prefered safety (1 war zone, 5 safest):\n"+DrawSkala(Preferences[2],Cur==4)+"\n   1    2    3    4    5\n")
    print("Imortance of safety (1 unimportant, 5 very important):\n"+DrawSkala(Importance[2],Cur==5)+"\n   1    2    3    4    5\n")


while True:
    PrintField(Cur)
    Move=getch.getch()
    if Move=="w" and Cur>0:
        Cur-=1
    if Move=="s" and Cur<5:
        Cur+=1
    if Move=="a" and Cur%2==0 and Preferences[Cur//2]>1:
        Preferences[Cur//2]-=1
    if Move=="a" and Cur%2==1 and Importance[Cur//2]>1:
        Importance[Cur//2]-=1
    if Move=="d" and Cur%2==0 and Preferences[Cur//2]<5:
        Preferences[Cur//2]+=1
    if Move=="d" and Cur%2==1 and Importance[Cur//2]<5:
        Importance[Cur//2]+=1
    if Move==" ":
        break

print(Preferences,Importance)





    