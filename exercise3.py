zele1=float(input("Enter a number for zele1:"))
zele2=float(input("Enter a number for zele2:"))
zele3=float(input("Enter a number for zele3:"))
if zele1>0 and zele2>0 and zele3>0:
    if zele1< zele2+zele3 and  zele2< zele1+zele3  and zele3< zele1+zele2:
    print("it is a mosalas")
    else:
    print("it is not a mosalas")
else:
    print("it is not a mosalas")
