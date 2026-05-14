#Python Banking Programme 

Amount=0
def deposit():
  global Amount
  print("------Deposit cash--------")
  while True:
     s=int(input("Enter The Deposit Amount: ₹"))
     Amount=Amount+s
     i=input("Want to add more:(Y/N): ")
     if i in "Nn":
        break
  print(f"The Updated Amount ₹{Amount}")
  return Amount
def withdraw():
   print("-------Withdraw Cash-----------")
   print("-------New Transaction---------")
   print("The Maximuim Amount you can withdraw is ₹5000 per Transaction")
   tr=0
   global Amount
   while True:
     s=int(input("Enter The Amount to be Withdrawn: ₹"))
     if s+tr>5000:
        print("The Amount should not exceed ₹5000")
     elif s>Amount:
        print("Imsufficient balance")
     else:
          Amount=Amount-s    
          tr=tr+s 
     o=input("Want To Withdraw More?(Y/N): ")
     if o in'Nn':
        break  
def show():
   if Amount<300:
      print(f"Your Current Balance ₹{Amount} is very Low")
   else:
      print(f"Your Current balance is ₹{Amount}")
while True:
   print("======WELCOME=======")
   print("======T-BANK========")
   print("--Enter Your Choice--")  
   d={"To Deposit Cash":"Press 1",
      "To Withdraw Cash":"Press 2",
      "To Show balance":"Press 3"}
   for key,value in d.items():
    print(f"{key:20}:{value:}")
   s=int(input("Enter your Choice: "))
   if s==1:
      deposit()
   elif s==2:
      withdraw()
   elif s==3:
      show()
   else:
      print("Choose a correct Option")



     