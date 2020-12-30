from tkinter import * 
import random
import datetime


# Events for Mainframe dealing with month and day scales 
def changeScale(self):
    a=month1Var.get()
    if a==2:
        day1Scale.config(to=28)
    else:
        day1Scale.config(to=31)
    b=month2Var.get()
    if b==2:
        day2Scale.config(to=28)
    else:
        day2Scale.config(to=30)

    fullname=fullnameCVar.get()
    fullnameLab.config(text=fullname, font=("Courier",20,"italic"))
    
    place= placeVar.get()
    loc.config(text=place)

# Events for Third Frame
# The code for car selection

def carSelection():
    print("car selection function started")
    a1=typeVar.get()
    b1=passVar.get()
    c1=budgetVar.get()
    d1=transVar.get()
    

# This is the code to manage sedan selection
    if a1=="Sedan":
        if b1==2:
            if c1>=40 and c1<70:
                if d1==0:
                    car1rbs.config(text=sedan[0], value=45)
                    car2rbs.config(text=sedan[1],value=46 )
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text=sedan[2], value=48)
                    car2rbs.config(text=sedan[3], value=67)
                    car3rbs.config(text=" ", value=0)
            elif c1>70 and c1<90:
                if  d1==0:
                    car1rbs.config(text=sedan[4], value=87)
                    car2rbs.config(text=sedan[5], value=76)
                    car3rbs.config(text=" ", value=0)
                else:
                    car1rbs.config(text=sedan[6], value=89)
                    car2rbs.config(text=" ", value=0)
                    car3rbs.config(text=" ", value=0)
            elif c1>90:
                if d1==0:
                    car1rbs.config(text=sedan[7], value=97)
                    car2rbs.config(text=sedan[8], value=143)
                    car3rbs.config(text=" ", value=0)
                else:
                    car1rbs.config(text=sedan[9], value=94)
                    car2rbs.config(text=" ", value=0)
                    car3rbs.config(text=" ", value=0)
        elif b1==4:
            if c1>=40 and c1<70:
                if d1==0:
                    car1rbs.config(text=sedan[0],value=56)
                    car2rbs.config(text=sedan[1], value=67)
                    car3rbs.config(text=" ", value=0)
                else:
                    car1rbs.config(text=sedan[2], value=67)
                    car2rbs.config(text=" ", value=0)
                    car3rbs.config(text=" ", value=0)
            elif c1>70 and c1<90:
                if  d1==0:
                    car1rbs.config(text=sedan[5], value=78)
                    car2rbs.config(text=" ", value=0)
                    car3rbs.config(text=" ", value=0)
                else:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>90:
                if d1==0:
                    car1rbs.config(text=sedan[7], value=99)
                    car2rbs.config(text=sedan[8], value=101)
                    car3rbs.config(text=" ", value=0)
                else:
                    car1rbs.config(text=sedan[9], value=100)
                    car2rbs.config(text=" ", value=0)
                    car3rbs.config(text=" ", value=0)
        elif b1==5:
            if c1>=40 and c1<70:
                if d1==0:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)                  
                else:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>70 and c1<90:
                if  d1==0:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>90:
                if d1==0:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)

##   
### End of code to manage sedan collection

# Managing SUV Collection

    elif a1=="SUV":
        if b1==2:
            if c1>=40 and c1<70:
                if d1==0:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>70 and c1<90:
                if d1==0:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>90:
                if d1==0:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.gconfig(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
        elif b1==4:
            if c1>=40 and c1<70:
                if d1==0:
                    car1rbs.config(text="Chrysler Pacifica", value=45)
                    car2rbs.config(text="Nissan Rogue", value=50)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text= "Chrysler Pacifica",value=67)
                    car2rbs.config(text="Nissan Rogue", value=69)
                    car3rbs.config(text=" ",value=0)
            elif c1>70 and c1<90:
                if d1==0:
                    car1rbs.config(text= "Jeep Cherokee",value=76)
                    car2rbs.config(text="Dodge Journey",value=80)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text= "GMC Yukon",value=88)
                    car2rbs.config(text="Nissan Pathfinder",value=80)
                    car3rbs.config(text=" ",value=0)
            elif c1>90:
                if d1==0:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text= "Ford Transit",value=99)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
        elif b1==5:
            if c1>=40 and c1<70:
                if d1==0:
                    car1rbs.config(text= "Dodge Caravan",value=56)
                    car2rbs.config(text="Dodge Durango",value=60)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text= "Dodge Durango",value=67)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>70 and c1<90:
                if d1==0:
                    car1rbs.config(text= "Toyota Highlander",value=89)
                    car2rbs.config(text="Toyota RAV 4",value=88)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text=" ",value=0)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>90:
                if d1==0:
                    car1rbs.config(text= "Yukon XL",value=100)
                    car2rbs.config(text="Mercedes GLK 450",value=134)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text= "Ford Flex",value=99)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
# End of SUV collection

# Green collection                
    elif a1=="Green":
        if b1==2:
            if c1>=40 and c1<70:
                if d1==0:
                    car1rbs.config(text="Toyota Prius",value=56)
                    car2rbs.config(text="Toyota Camary",value=66)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="Toyota Prius",value=55)
                    car2rbs.config(text="Toyota Camary",value=67)
                    car3rbs.config(text=" ",value=0)
            elif c1>70 and c1<90:
                if d1==0:
                    car1rbs.config(text="Chrysler 300",value=78)
                    car2rbs.config(text="Chrysler 300C",value=88)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="Chevrolet Sonic",value=79)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>90:
                if d1==0:
                    car1rbs.config(text="Toyota Yarris",value=96)
                    car2rbs.config(text="Honda Civic Gt",value=93)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="Ford Fusion",value=145)
                    car2rbs.config(text=" ",value=0)
                    car3rbs.config(text=" ",value=0)
        elif b1==4:
             if c1>=40 and c1<70:
                if d1==0:
                    car1rbs.config(text="Chevrolet Sonic",value=45)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="Toyota Yarris Ext",value=55)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
             elif c1>70 and c1<90:
                if d1==0:
                    car1rbs.config(text="Corvette Z06",value=77)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="Corvette Stingray",value=88)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
             elif c1>90:
                if d1==0:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
        elif b1==5:
            if c1>=40 and c1<70:
                if d1==0:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>70 and c1<90:
                if d1==0:
                    car1rbs.config(text="Honda GTR 360",value=76)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="Toyota Camary Lux 2018",value=78)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>90:
                if d1==0:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)

#End of Green Collection
                                   
# Dream Cars
    elif a1=="Con":
        if b1==2:
            if c1>=40 and c1<70:
                if d1==0:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>70 and c1<90:
                if d1==0:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>90:
                if d1==0:
                    car1rbs.config(text="Porshe 911",value=145)
                    car2rbs.config(text="Porshe Boxter",value=149)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="Nissan GTR",value=134)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
        elif b1==4:
             if c1>=40 and c1<70:
                if d1==0:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
             elif c1>70 and c1<90:
                if d1==0:
                    car1rbs.config(text="Mercedes C63",value=76)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="Porche 911",value=83)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
             elif c1>90:
                if d1==0:
                    car1rbs.config(text="Porshe Macan",value=123)
                    car2rbs.config(text="Porshe Cayman",value=143)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="Mercedes CLA",value=145)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
        elif b1==5:
            if c1>=40 and c1<70:
                if d1==0:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="",value=0)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>70 and c1<90:
                if d1==0:
                    car1rbs.config(text="Porshe Macan",value=76)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                else:
                    car1rbs.config(text="Porshe Cayenne",value=88)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
            elif c1>90:
                if d1==0:
                    car1rbs.config(text="Range Rover Sport",value=99)
                    car2rbs.config(text="Porshe Panamera",value=88)
                    car3rbs.config(text=" Land Rover",value=99)
                else:
                    car1rbs.config(text="Tesla Model X",value=98)
                    car2rbs.config(text="",value=0)
                    car3rbs.config(text=" ",value=0)
                        
# This is for the price summary

def cost():
    # Calculating Car cost based on number of days 
    a=month1Var.get()
    b=day1Var.get()
    c=month2Var.get()
    d=day2Var.get()
    carvalue=matchVar.get()

    # today = datetime.date.today()
    startdate = datetime.date(2018, a, b)
    returndate= datetime.date(2018, c, d)

    diff = (returndate - startdate).days

    carcost= (carvalue*diff)
    
    # Adding additional costs
    E1= boostVar.get()
    E2=auxVar.get()
    E3=gpsVar.get()
    E4=speedwarVar.get()
    additionalcosts= (E1+E2+E3+E4)

    # This is total cost including the days and extras
    total1= int(carcost) + int(additionalcosts)
    print("Total1",total1)

    #if he/she is a member
    promo= membVar.get()
    if promo=="00000":
        total1=0.8*(total1)
        grandVar.set(f' $ {total1:.2f}')
    else:
        total1= (carcost+ additionalcosts)
        grandVar.set(f' $ {total1:.2f}')

            

 # Creating The Frames            
root = Tk()
mainframe = Frame(root)



secondframe= Frame(root)



thirdframe= Frame(root)


fourthframe= Frame(root)







#Creating the Widgets

#This is for the Mainframe/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#This is the Name of the Car Rental
nameLabel= Label(mainframe, text="Carz Rental", font=("Courier", 30, "bold"), fg="red" )

#This is the pick up location Label
pickLabel=Label(mainframe,  text="Pick Up Location", font=("Courier", 10, "bold") )

#Pick Up Location Option Menu
pickups= ["Brookfield Place","BBT Airport","North York","Hudson Centre","Pearson Airport"]
placeVar= StringVar()
pickupOm= OptionMenu(mainframe, placeVar, *pickups, command=changeScale)

#Pick Up Date Scales and frame and label
pickUpFrame=LabelFrame(mainframe, text="Pick Up Date", font=("Courier", 10, "bold"))
month1Var= IntVar()
month1Var.set(1)
month1Scale= Scale(pickUpFrame, variable= month1Var, from_=1,to=12, showvalue= True, label="Month", length=100, width=10, orient=HORIZONTAL,command=changeScale)

day1Var=IntVar()
day1Var.set(1)
day1Scale=  Scale(pickUpFrame, variable=day1Var, from_=1,to=31, showvalue= True, label="Day", length=100, width=10, orient=HORIZONTAL)

#Return Date Scales, label and frame
returnFrame=LabelFrame(mainframe,  text=" Return Date", font=("Courier", 10, "bold"))
month2Var= IntVar()
month2Var.set(1)
month2Scale= Scale(returnFrame, variable= month2Var, from_=1,to=12, showvalue= True, label="Month", length=100, width=10, orient=HORIZONTAL)

day2Var=IntVar()
day2Var.set(1)
day2Scale=  Scale(returnFrame, variable=day2Var, from_=1,to=31, showvalue= True, label="Day", length=100, width=10, orient=HORIZONTAL)

#Customer Age Label and Entry Box
ageLabel= Label(mainframe, text="Age", font=("Courier", 10, "bold"))

ageCVar= StringVar()
ageEntry= Entry(mainframe,  width=15,textvariable= ageCVar)

# fullname Label and Entry Box
fullnameLabel= Label(mainframe, text="Full Name", font=("Courier", 10, "bold"))
fullnameCVar= StringVar()
fullnameEntry= Entry(mainframe, textvariable= fullnameCVar, width=15)



# This is for the Second Frame

# Car Type Question Label, frame and Radiobuttons
carframe= LabelFrame(secondframe, text="Types of Cars",  font=("Courier", 10, "bold"))
typeVar= StringVar()
typeVar.set("Sedan")
sedrb=Radiobutton(carframe,text="Sedan", variable= typeVar, value="Sedan")
suvrb= Radiobutton(carframe, text= "SUVs", variable= typeVar, value= "SUV")
greenrb= Radiobutton(carframe, text=" Green Collection", variable=typeVar, value="Green")
convrb= Radiobutton(carframe, text="Dream Cars", variable= typeVar, value="Con")

# How many Passengers Label, Label Frame and RadioButtons
passFrame=LabelFrame(secondframe, text="# of Passengers" ,font=("Courier", 10, "bold"))
passVar= IntVar()
passVar.set(2)
tworb= Radiobutton(passFrame, text=" 2 Passengers", variable=passVar, value=2)
fourrb= Radiobutton(passFrame, text=" 4 Passengers", variable=passVar, value=4)
morerb= Radiobutton(passFrame, text=" 4+ Passengers", variable= passVar, value=5)

# Transmission Label, Frame and RadioButtons
transFrame= LabelFrame(secondframe, text=" Transmission", font=("Courier", 10, "bold"))
transVar= IntVar()
transVar.set(1)
Manrb= Radiobutton(transFrame, text= "Manual", variable= transVar, value=0)
Autorb= Radiobutton(transFrame, text= "Automatic",variable= transVar, value=1)

#Budget Scale and Label
budgetLabel= Label(secondframe, text= " Your Budget ($/Day)",font=("Courier", 10,"bold"))
budgetVar= IntVar()
budgeScale= Scale(secondframe, orient=HORIZONTAL, from_=40,to= 150, showvalue=True,variable=budgetVar, width=20, length=160 )

#Button to search for matches
searchButton= Button(secondframe,text="Find My Car", font=("Courier", 15, "bold"), fg="blue", command=carSelection )


#This is for the third frame
# Sedan
sedan=["Chevrolet Spark","Ford Focus","Nissan Versa","Volkswagen Passat","Mazda 3"," Volkswagen Jetta","Chevrolet Malibu","Buick Regal","Dodge Challenger","Lincoln Continental"]
#This is are the results based on what the user wants (Includes labels, label frame and radio button)
matchLabel= Label(thirdframe, text=" These are your matches", font=("Courier", 10) )
matchFrame= LabelFrame(thirdframe, text="Matches", font=("Courier", 10, "bold"))
matchVar= IntVar()
car1rbs= Radiobutton(matchFrame, text="", variable=matchVar, value=1)
car2rbs= Radiobutton(matchFrame, text="", variable= matchVar, value=2)
car3rbs= Radiobutton(matchFrame, text="", variable= matchVar, value=3)

#This is for the Extras
extraFrame= LabelFrame(thirdframe, text= "Extras" ,font=("Courier", 10, "bold"))
boostVar= IntVar()
boostercb= Checkbutton(extraFrame, text= "Booster Seats", variable=boostVar, onvalue=100, offvalue=0)
auxVar= IntVar()
auxcb= Checkbutton(extraFrame, text=" AUX Cables", variable= auxVar, onvalue=10, offvalue=0)
gpsVar=IntVar()
gpscb= Checkbutton(extraFrame, text="G.P.S", variable= gpsVar, onvalue=100, offvalue=0)
speedwarVar= IntVar()
speedcb= Checkbutton(extraFrame, text=" Speed Warranty", variable= speedwarVar, onvalue=50, offvalue=0)



# Membership Entry and Label
memLab=Label(thirdframe, text=" Are You a Member? If yes, \n enter your id # -->(00000)",  font=("Courier", 10, "bold"))
membVar= StringVar()
memberEnt= Entry(thirdframe,width=15,textvariable= membVar)

#Information exlusion label
infoLab= Label(fourthframe, text= "When the Matches box is empty \n there are no matches found for your \n searches",  font=("Courier", 10, "bold"))


# Total Price and summary
Sumframe= LabelFrame(fourthframe, text="  Summary" ,font=("Courier", 10, "bold"))

# Cost Button
costB= Button(fourthframe, text= "Lets Calculate the cost", command=cost, font=("Courier", 15, 'bold'), fg="blue")

# Total Price Label
grandtotal= Label(Sumframe, text="Grand Total(Incl.Tax) : ")

grandVar= IntVar()
grandLab= Label(Sumframe, textvariable=grandVar)

# Pick Up Location
locPlace= Label(Sumframe, text="Pick Up Location:")
loc= Label(Sumframe, text=" ")

# Cost Inclusions
inclusionLab= Label(Sumframe, text="The Cost Includes:")

information= Label(Sumframe, text= "Cost, extras ,discount")

# fullname Lab
fullnameLab= Label(fourthframe, text=" ")

#Thanks
thanksLab= Label(fourthframe, text="Thank you \n for selecting our services \n Promo Code for 45% \n discount==>67253 \n NEXT TIME",font=("Courier", 10))






# Griding the Widgets
# This is the mainframe or the first frame //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
mainframe.grid(row=1,column=1, padx=10,pady=10, sticky=N)
nameLabel.grid(row=1, column=1, columnspan=3, pady=10)

fullnameLabel.grid(row=2, column=1, sticky=W)
fullnameEntry.grid(row=2, column=2, sticky= W+E, pady=10)

ageLabel.grid(row=3, column=1, sticky=W)
ageEntry.grid(row=3, column=2, sticky=W+E, pady=10)

pickLabel.grid(row=4, column=1, sticky= W, pady=10)
pickupOm.grid(row=4, column=2, sticky=W+E, pady=10)

pickUpFrame.grid(row=5, column=1, sticky=W+E, columnspan=2, pady=20)
month1Scale.grid(row=1, column=2, sticky=E, padx=10)
day1Scale.grid(row=2, column=2, sticky= E, padx=10)

returnFrame.grid(row=6, column=1, sticky=W+E, columnspan=2, pady=20)
month2Scale.grid(row=1, column=2,sticky=E, padx=10)
day2Scale.grid(row=2, column=2, sticky=E, padx=10)



#  This is the second frame /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
secondframe.grid(row=1,column=2,padx=10,pady=10)
# Car Type Label, frame and Radiobuttons
# carTypeLabel.grid(row=2, column=1, columnspan=2)
carframe.grid(row=2, column=1, sticky=W+E,  pady=10, columnspan=2)
sedrb.grid(row=1, sticky=W)
suvrb.grid(row=2, sticky=W)
greenrb.grid(row=3, sticky=W)
convrb.grid(row=4, sticky=W)
#Transmission
##transLabel.grid(row=4, column=2, sticky=W, padx=10)
transFrame.grid(row=3, column=1, sticky=W+E, pady=10, columnspan=2)
Manrb.grid(row=1, sticky=W)
Autorb.grid(row=2, sticky=W)
# How many Passengers Label, Label Frame and RadioButtons
##passLabel.grid(row=4, column=1, sticky=W, pady=10)
passFrame.grid(row=4, column=1, sticky=W+E, columnspan=2, pady=10)
tworb.grid(row=1, sticky=W)
fourrb.grid(row=2, sticky=W)
morerb.grid(row=3, sticky=W)

# Budget
budgetLabel.grid(row=5, column=1, sticky=E+W,rowspan=2, padx=10, pady=(10,10))
budgeScale.grid(row=6, column=2, sticky=E+N, pady=(10,10))
#Search Button
searchButton.grid(row=7, column=1, sticky=W+E+S, columnspan=4, pady=10)


# This is for the third frame////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
thirdframe.grid(row=1, column=3,padx=10,pady=10)

# This is the matches frame, label and radiobuttons
matchFrame.grid(row=2, column=1, sticky=E+W+S, columnspan=20,pady=10)
car1rbs.grid(row=1,sticky=W)
car2rbs.grid(row=2, sticky=W)
car3rbs.grid(row=3, sticky=W)




# This includes the extras frame and checkbuttons
extraFrame.grid(row=3, column=1, sticky= W+E+S, columnspan=2, pady=60)
boostercb.grid(row=1, sticky=W)
auxcb.grid(row=2, sticky=W)
gpscb.grid(row=3, sticky=W)
speedcb.grid(row=4,sticky=W)

# This includes membership options
memLab.grid(row=4, column=1,sticky=W, pady=30)
memberEnt.grid(row=4, column=2, sticky=E, pady=30)


costB.grid(row=5, column=1, pady=(20,5), columnspan=2, sticky=S)


# This is for the fourthframe
fourthframe.grid(row=1, column=4, padx=10,pady=10)
## Price and summary
costB.grid(row=1, column=1, pady=15, columnspan=2, sticky=W)
infoLab.grid(row=2, column=1, sticky=E+W, columnspan=2, pady=20)
Sumframe.grid(row=3, column=1, pady=20, sticky=W+E)
grandtotal.grid(row=1, column=1, sticky=W)
grandLab.grid(row=1, column=2, sticky=W)
locPlace.grid(row=2, column=1, sticky=W)
loc.grid(row=2, column=2, sticky=W)
inclusionLab.grid(row=3, column=1, sticky=W)
information.grid(row=4, column=1, sticky=W)


fullnameLab.grid(row=4,column=1, sticky=W+E, pady=10, padx=15)
thanksLab.grid(row=5, column=1, sticky=W+E, columnspan=2, pady=10, padx=10)


























































                 

