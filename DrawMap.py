from os import system as x
# pip install py-getch
import getch

#inputing size of the map. Only integers greater than 1 are allowed
while True:
   try:
      sx=int(input("Size x? "))
   except ValueError:
       continue   
   if (sx>1):
       break
while True:   
    try:
      sy=int(input("Size y? "))
    except ValueError:
       continue 
    if (sy>1):
       break

#elements of the map

top="┌───"+"┬───"*(sx-2)+"┬───┐\n"
middle="│   "*sx+"│\n"
midrow="├───"+"┼───"*(sx-2)+"┼───┤\n"
bottom="└───"+"┴───"*(sx-2)+"┴───┘\n"


def mid_insert(i,sx):    # puts an X in the ith column 
    return "│   "*i+"│ X "+"│   "*(sx-1-i)+"│\n"
def print_coord(i,j,sx,sy):    #creates a map with x in the ith column and jth row
    if j<sy-1:
        print(top+(middle*3+midrow)*j+middle+mid_insert(i,sx)+middle+midrow+(middle*3+midrow)*(sy-2-j)+middle*3+bottom)
    else:
        print(top+(middle*3+midrow)*j+middle+mid_insert(i,sx)+middle+bottom)
i=0
j=0

x("clear")
print_coord(i,j,sx,sy)  
print("w,a,s,d,x?")

#walks the map

while True:
    
    direct=getch.getch()
    if direct=="w":
        if j>0:
            j-=1
    if direct=="a":
        if i>0:
            i-=1
    if direct=="s":
        if j<sy-1:
            j+=1
    if direct=="d":
        if i<sx-1:
            i+=1
    if direct=="x":
        break
    x("clear")
    print_coord(i,j,sx,sy)        
    print("w,a,s,d,x?")
    