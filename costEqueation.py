import math

category = ["lorry","car","3wheel","bike"]

costDictionary = {
    "sedan":9.1,
    "micro":8.05,
    "piagio ape": 3.4,
    "bajaj":4.8,
    "ct100":1.5,
    "scooty":3.5
}

def Vcat( category ):
        switcher={
                "lorry":0,
                "car":1,
                "3wheel":2,
                "bike":3             }
        
        return switcher.get(category,"Invalid vehicle category")
    
def Vtyp(cat):
        switcher={
                0:["Big lorry","Dimo batta"],
                1:["Sedan","Micro"],
                2:["Piagio ape","Bajaj"],
                3:["CT100","Scooty"]        }
        
        return switcher.get(cat)

def typ():
    return (input('\n'*1 +"Enter " +category[cat] + " type, " + Vtyp(cat)[0] + " or "+ Vtyp(cat)[1] +" ? ")).lower()

def validator(v):
    return not((v == Vtyp(cat)[0].lower()) or (v == Vtyp(cat)[1].lower()))
    

def maintananceCost(vt):
    while True:
        num = input('\n'*1 +"Enter maintance cost of "+vt+" per 1 kilometer >> ")
        try:
            val = int(num)
            return val
            break;
        except ValueError:
            print("This is not a number. Please enter a valid number")

def totalCost(vt,mtCost):
    x = math.ceil(float(costDictionary[vt]+mtCost))
    print ('\n'*1 + "Great! your total approximate cost of 1km for "+vt+" type of "+category[cat]+" is Rs: "+str(x))

def vCategory():
    return Vcat(category = (input('\n'*1 +"Enter vehicle category >>  ")).lower())
    
#---------------------------------------------------------------------------------    
#GamePlay starts from here
#---------------------------------------------------------------------------------
cat = vCategory()
while(cat=="Invalid vehicle category"):
    print(cat)
    cat = vCategory()
    
print("You have selected "+category[cat]+" category")
#---------------------------------------------------------------------------------

vehicleType = typ()
xex = validator(vehicleType)

while(xex):
    print("Invalid "+category[cat]+" type")
    vehicleType = typ()
    xex = validator(vehicleType)

print("You have selected "+vehicleType+" type of vehicle in "+category[cat]+" category")
#----------------------------------------------------------------------------------

maintananceCost = maintananceCost(vehicleType)
#final output
totalCost(vehicleType,maintananceCost)
