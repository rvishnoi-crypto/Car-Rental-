from tkinter import *
import random

def storingCall():
   
    ActualService=serviceVar.get()
    ActualUsername=userVar.get()
    ActualPassword= passVar.get()

    storingFunctionality(ActualService,ActualUsername,ActualPassword)

def storingFunctionality(serviceSelected,usernameSelected,passwordSelected):
    global services,username, password
    services.append(serviceSelected)
    username.append(usernameSelected)
    password.append(passwordSelected)

    print(services,username,password, "hello")



def retrievingCall():
    StoreService=serviceVar.get()

    retrievingFunctionality(StoreService)
    

def retrievingFunctionality(serviceSelected):
    global services,username, password
    for i in services:
        if i==serviceSelected:
            a=services.index(i)
            print(a)
            userVar.set(username[a])
            print(username[a])
            passVar.set(password[a])
    

def clrCredentials():
    global services,username, password
    serviceVar.set(" ")
    userVar.set(" ")
    passVar.set(" ")
    print(services,username,password, "Test")

def ScoreGenerator():
    # using the value returned from other function
    TruePassword=passVar.get()
    TrueUsername=userVar.get()
    TrueService=serviceVar.get()
    
    Score_Rule1=scoring_based_on_Rule1(TruePassword)
    print(Score_Rule1)
    Score_Rule2=scoring_based_on_Rule2(TruePassword)
    print(Score_Rule2)
    Score_Rule3=scoring_based_on_Rule3(TruePassword)
    print(Score_Rule3)
    grandScore=100
    grandScore-=(Score_Rule1+Score_Rule2+Score_Rule3)
    scoreVar.set(grandScore)

    if grandScore==0:
        strengthVar.set(" ")
    elif grandScore<70:
        strengthVar.set("Average")
    elif grandScore>70 and grandScore<85:
        strengthVar.set("Good")
    else:
        strengthVar.set("Excellent")
    
 
def scoring_based_on_Rule1(passwordSelected):
    #This is based on the length
    totalScore1=0
    wordLength=len(passwordSelected)

    if wordLength>1 and wordLength<8:
        totalScore1 +=20
    elif wordLength>8:
        totalScore1 +=0
    return totalScore1

def scoring_based_on_Rule2(passwordSelected):
    #This is based on the symbols
    totalScore2=0
    symbols=0
    for i in passwordSelected:
        if (ord(i)>32 and ord(i)<47 )or (ord(i)>57 and ord(i)<65):
            symbols+=1
    if symbols<1:
        totalScore2+=20
    elif symbols==1 or symbols>1:
        totalScore2+=0
    return totalScore2

def scoring_based_on_Rule3(passwordSelected):
    #This is based on repititions
    totalScore3=0
    lengthOfWord= len(passwordSelected)
    repitition=0
    for i in range(1,lengthOfWord):
        if ord(passwordSelected[i])==ord(passwordSelected[i-1]):
            repitition+=1
    print("Repititions", repitition)
    if repitition==0:
        totalScore3+=0
    else:
        totalScore3+=20
    return totalScore3

def generateNewPasswordCall():
    givenPass= passVar.get()
    GeneratedPassword=generateNewPasswordFunctionality(givenPass)

    generateVar.set(GeneratedPassword)
     

def generateNewPasswordFunctionality(Password):
    newPassword=Password
    #This password will be generated even if the user gets a strength of 100
    #This is based on character length 
    LengthofWord=len(newPassword)
    while(LengthofWord<8):
            randomAscii= random.randint(64,79)
            newPassword=(newPassword)+ str(chr(randomAscii))
            LengthofWord=len(newPassword)


    #This is based on symbols
    NumofSymbols=0
    for i in newPassword:
        if ( 32<ord(i)<48 ) or (57<ord(i)<65):
            NumofSymbols+=1
            

    if NumofSymbols<1:
        randomSymbol=random.randint(33,47)
        newPassword=newPassword+str(chr(randomSymbol))


    #This is based on repitition
    rep=0
    LengthofWord=len(newPassword)

    print( 'newpassword=', newPassword, 'length=',LengthofWord)

    for i in range(1,LengthofWord):
        print('i=',i, 'rep=', rep, 'letter', newPassword[i], 'newpassword=', newPassword)
        if ord(newPassword[i])==ord(newPassword[i-1]):
            print('inside if whats the letter matching', newPassword[i])
            newPassword= newPassword[:i]+ str(chr(ord(newPassword[i-1])+1)) + newPassword[i:]
            LengthofWord+=1
            print ('what is the new password', newPassword,)
            rep+=1
        print('# of repeats= ',rep)
    

    
    print(newPassword)

    return newPassword

def PasswordUserCall(event):
    passToUse=generateVar.get()
    PasswordUserFunctionality(passToUse)

def PasswordUserFunctionality(passwordToUse):
    passVar.set(passwordToUse)
        

root=Tk()

# This is the creation of frames
mainframe= Frame(root)
secondframe=Frame(root)
thirdframe= Frame(root)

# Creating Widgets for mainframe////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# This is the heading
headingLab= Label(mainframe, text= "Password Generator", font=("Courier",20))

# This is the service entry box and service label
serviceVar= StringVar()
serviceLab= Label(mainframe, text="Service", font=("Courier",10))
serviceEnt= Entry(mainframe, textvariable=serviceVar)

# This is the Username Label and Entry Box
userLab= Label(mainframe, text="Username", font=("Courier",10))
userVar= StringVar()
userEnt= Entry(mainframe, textvariable=userVar)

# This is the Password Label and Entry Box
passLab= Label(mainframe, text="Password", font=("Courier",10))
passVar= StringVar()
passEnt= Entry(mainframe, textvariable=passVar)
passEnt.bind("<Button-1>",PasswordUserCall)


# This is the store, retrieve and clr button
storeButton= Button(mainframe, text="Store Credentials", command=storingCall)
retrieveButton= Button(mainframe, text="Retreive Crendentials", command=retrievingCall)
clrButton=Button(mainframe, text="Clear Credentials", command=clrCredentials)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

 # Creating Widgets for secondframe//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

 #This is the score Button and score Label
scoreButton= Button(secondframe, text="Score My Password",command=ScoreGenerator)
scoreVar= IntVar()
scoreVar.set(0)
scoreLab= Label(secondframe, textvariable= scoreVar,  font=("Courier",10))

 # This is the password strength and password strength label
strengthLab= Label(secondframe,text="Password Strength",font=("Courier",10))
strengthVar= StringVar()
strengthVar.set(" ")
displayLab= Label(secondframe, textvariable=strengthVar)

# This is the Generate Button and the generated password 
generateButton= Button(secondframe, text="Generate New Password",command=generateNewPasswordCall)
generateVar= StringVar()
generateVar.set("")
newPassLab= Label(secondframe, textvariable=generateVar)

#This is the information Label
infoLab= Label(secondframe, text="left Click on Password Entry to use Password", font=("Courier",10),fg="#1a2ec9")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Creating Widgets for thirdframe

# Creating a Label frame for the rules
rulesFrame= LabelFrame(thirdframe)
rulesInfoLab= Label(thirdframe, text= "Password Requirements", font=("Courier", 15))

#Rules in the frame
rulesLab= Label(rulesFrame, text="1. Have Atleast 8 Characters \n\n2. Have Atleast 1 Symbol \n\n 3. No consecutive  repitions")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#GRIDING THE WIDGETS FOR MAINFRAME
mainframe.grid(row=1,column=1,padx=10,pady=10)

#Griding the heading 
headingLab.grid(row=1, column=1, columnspan=2, padx=10)

#Griding the service, username, password label and entry boxes
serviceLab.grid(row=2, column=1, sticky=W,pady=10)
serviceEnt.grid(row=2, column=2, sticky=W+E, pady=10)

userLab.grid(row=3, column=1,sticky=W,pady=10)
userEnt.grid(row=3, column=2, sticky=W+E, pady=10)

passLab.grid(row=4, column=1,sticky=W, pady=10)
passEnt.grid(row=4, column=2, sticky=W+E, pady=10)

#Griding the store, retrieve and clr button
storeButton.grid(row=5, column=1, columnspan=2, sticky=W+E, pady=10)
retrieveButton.grid(row=6, column=1,columnspan=2, sticky=W+E, pady=10)
clrButton.grid(row=7, column=1, columnspan=2, sticky=W+E, pady=10)


#GRIDING THE WIDGETS FOR THE SECOND FRAME
secondframe.grid(row=1,column=2, padx=10,pady=10)

# Griding the Score button and label
scoreButton.grid(row=1, column=1, columnspan=2, sticky=W+E+N, pady=10)
scoreLab.grid(row=2, column=1, columnspan=2)

# Griding the password strength label and display label
strengthLab.grid(row=3, column=1,sticky=W, pady=20)
displayLab.grid(row=3, column=2, sticky=E, pady=10, padx=20)

#Griding the Generate New Password button and new pass lab
generateButton.grid(row=4, column=1, columnspan=2, sticky=W+E, pady=10)
newPassLab.grid(row=5, column=1, columnspan=2, pady=10)

#Griding Extra Information and event
infoLab.grid(row=6, column=1, pady=5)


#GRIDING THE WIDGETS FOR THE THIRD FRAME
thirdframe.grid(row=1, column=3, padx=10, pady=10)

#Griding the Label Frame for rules
rulesInfoLab.grid(row=1, column=1, columnspan=2)
rulesFrame.grid(row=2, column=1, columnspan=2,rowspan=3, pady=50)
rulesLab.grid(row=1, sticky=W)


#Main

#These are the list which will be used to store and retreive credentials
global services,username, password
services=[]
username=[]
password=[]

















