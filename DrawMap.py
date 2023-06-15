from os import system as x
import getch

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

top="┌───"+"┬───"*(sx-2)+"┬───┐\n"
middle="│   "*sx+"│\n"
midrow="├───"+"┼───"*(sx-2)+"┼───┤\n"
bottom="└───"+"┴───"*(sx-2)+"┴───┘\n"

#print(top+(middle*3+midrow)*3+middle*3+bottom)
def mid_insert(i,sx):
    return "│   "*i+"│ X "+"│   "*(sx-1-i)+"│\n"
def print_coord(i,j,sx,sy):
    if j<sy-1:
        print(top+(middle*3+midrow)*j+middle+mid_insert(i,sx)+middle+midrow+(middle*3+midrow)*(sy-2-j)+middle*3+bottom)
    else:
        print(top+(middle*3+midrow)*j+middle+mid_insert(i,sx)+middle+bottom)
i=1
j=1

x("clear")
print_coord(i,j,sx,sy)  
print("w,a,s,d,x?")
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
    