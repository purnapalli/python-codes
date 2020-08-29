s=input("Enter requred string : ")
s1=s2=op=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    op=op+x
for x in sorted(s2):
    op=op+x
print("After sorting")
print(op)
