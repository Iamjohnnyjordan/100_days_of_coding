# if else elif statments with and without conditions 
print("Welcome to Papa Oom Mow Mow's Pizza!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
oom_mow_mow_sauce = input("Would you like a side of Oom Mow Mow Sauce hold the anchovies? Y or N:")


bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25


if pepperoni =="Y":
        if size == "S":
            bill += 2
        else:
            bill += 3

if extra_cheese =="Y":
    bill += 1

if oom_mow_mow_sauce =="Y":
    bill += .50

print(f"Your final bill is: ${bill:.2f}.")

