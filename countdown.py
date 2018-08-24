daysLeft = input("How many days until election day? ")
userInput = int(daysLeft)

while (userInput >= 0):
    userInput = userInput - 1
    if userInput >= 2:
        print(str(userInput) + " days until Election Day 2018!")
    elif userInput == 1:
        print(str(userInput) + " more day until Election Day 2018!")
    elif userInput == 0:
        print("It's Election Day 2018!")
        break
