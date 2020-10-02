 # following functions are defined default ,display, create(in create:- existing_status )
def default():
   print("hello.. admin")
def display():
   print("1.Add new status ")
   print("2.Choose  from existing statuses..")
def existing_status():
   print("1. At home..")
   print("2. DND")
   print("3. Hey..m here..")
def making_new_friend():
   
   ans = input("do you want to add new friends "+ "\n" + " Yes or No ")
   if(ans == "Yes"):
       new_Name = input("enter the name of friend:- ")
       print("your friend " + new_Name + "  is added")
   elif(ans == "No"):
       print("ok,see u later...")
       
       
def create():
   name=input("enter your name:- ")
   print("hello.." + name )
   passwrd=input("enter the valid password (It should contain one numerical digit,any symbol,and a capital letter):- ")
   confirm = input("re-enter your password:- ")
   if(confirm==passwrd):
       print("Password is set succesfully")
   else:
       print("re-enter your password")
   age = input("Enter your age:- ")
   proper_age = int(age)
   if(proper_age<12 or proper_age>50):
       print(" not eligible..")
   else:
       print("welcome")
       print("welcome..Dear "+ name + "__" + age +"...." + "welcome to spychat")
       display()
       to_do = int(input("to make your profile attractive choose any one:- "))
       if(to_do==1):
           status_input1 = input("write new status:- ")
           print("your status is updated:- " + status_input1)
       elif(to_do==2):
           existing_status()
           Enter_Choice = int(input("select any one:- "))
           if(Enter_Choice == 1):
               print("Your status is updated to:- " + "\n" + "At home..")
           elif(Enter_Choice == 2):
               print("Your status is updated to:- " + "\n" + "DND..")
           elif(Enter_Choice == 3):
               print("Your status is updated to:- " + "\n" + "Hey..m here..")
   making_new_friend()
print("hello.. my name is Aman ")
enter = int(input("do want to continue with default user or create your own press 1 or 2 resp:- "))   #taking input from user
if(enter == 1):
   default()     #default function  is called
elif(enter==2):
   create()      #create function is called