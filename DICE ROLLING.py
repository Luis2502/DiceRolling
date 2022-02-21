import random
while True:
    user = int(input("Do you want to roll the dice?\n1 - Roll\n2 - No\nEnter your choice: "))

    if user == 1:
        print ("1st dice: ",random.randint(1,6))
        print ("2nd Dice: ",random.randint(1,6))

    else:
        print("Thank you!")