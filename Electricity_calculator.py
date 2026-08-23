# Get the input from the user
units=int(input("Enter the units:"))
connection_type=input("either commercial or non-commercial:")
# calculate the non-commercial units and commercial
if(connection_type=="non-commercial"):
    if (units<=200):
        print("Free no charge")
    elif (units>=201 and units<=500):
        rem=units-200
        totalbill=rem*4
        print( "Rs-",totalbill)
    elif(units>=501 and units<=2000):
        rem=units-200
        totalbill=rem*8
        print("Rs-",totalbill)
    else:
        rem=units-200
        totalbill=rem*10
        print("Rs-",totalbill)
else:
    if(units<=500):
        totalbill=units*6
        print("Rs-",totalbill)
    elif(units>=501 and units<=1000):
        totalbill=units*9
        print("Rs-",totalbill)
    elif(units>=1001 and units<=5000):
        totalbill=units*12
        print("Rs-",totalbill)
    else:
        totalbill=units*15
        print("Rs-",totalbill)