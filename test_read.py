
database={}
with open("database.txt") as f:
    string=f.read().replace("\t","").splitlines()
    print(len(string))
    for i in range(0,len(string),6):
        print(i)
        database[string[i]]={"Information":string[i+1],"Climate":int(string[i+2]),"Price":int(string[i+3]),"Safety":int(string[i+4])}
    print(database)