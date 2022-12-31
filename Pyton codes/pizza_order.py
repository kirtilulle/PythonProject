# pizza order program
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill=0
if size == "S":
    bill +=150
elif size =="M":
    bill +=200
else :
    bill +=250

if add_pepperoni == "Y":
    if size == "S":
        bill +=20
    else:
        bill +=30
    
if extra_cheese == "Y":
    bill +=15

print(f" Your final bill is: {bill} rupees.")



    

