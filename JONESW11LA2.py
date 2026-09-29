print("================")
print("Pizza Flavor ")
print("================")
print("Watermelon Pizza")
print("Veggie Pizza")
print("White Pizza")
print("Cheese Pizza")
print("Hawaiian Pizza")
print("================")
print("Sizes (Small/Medium/Large)")
print("================")

# listahan sa utang ni bawi

Jonesflavor1 = [
    ("hawaiian", 499, 750, 1200),
    ("cheese", 399, 600, 999),
    ("veggie", 450, 700, 1100),
    ("white", 480, 720, 1800),
    ("watermelon", 500, 800, 1500)
]

Jonesflavor = input("Enter a Pizza Flavor: ").lower()
Jonessize = input("Enter size (Small/Medium/Large): ").lower()

Jonesprice = 0
# conditions na diri
print("===Receipt Price====")
for pizza in Jonesflavor1:
    if pizza[0] == Jonesflavor:
        if Jonessize == "small":
            Jonesprice = pizza[1]
        elif Jonessize == "medium":
            Jonesprice = pizza[2]
        elif Jonessize == "large":
            Jonesprice = pizza[3]
        else:
            print("Invalid size")
            print("Please Try Again!")
        break

else:
    print("Invalid Pizza Flavor")
# resibo
if Jonesprice > 0:
    print(f"{Jonesflavor.capitalize()} Pizza")
    print(f"Price: {Jonesprice}")
    print("Thank you for Purchasing")
    print("======================")




