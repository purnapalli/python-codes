rec={}
ans=True
while ans:
    rec.clear()
    name=input("Enter student name: ")
    percent=eval(input("Enter percentage % :"))
    rec[name]=percent
    if percent <=60:
        print("Result fail")
        continue
    print("\tStudent\t\tpercentage\t result")
    print('--------------------------------')
    P='Pass'
    for x in rec:
     print("\t",x,"\t\t",rec[x],"\t",P)
    ans=eval(input("You want to continue [True/False]: "))






