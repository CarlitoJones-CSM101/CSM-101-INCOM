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
Jonesflavor = input("Enter a Pizza Flavor: ").lower()
Jonessize = input("Enter size (Small/Medium/Large): ").lower()

Jonesprice = 0

print("===Receipt Price====")

match Jonesflavor:
    case "hawaiian":
        if Jonessize == "small":
            Jonesprice = 499
        elif Jonessize == "medium":
            Jonesprice = 750
        elif Jonessize == "large":
            Jonesprice = 1200
        else:
            print("Invalid size")
            print("Please Try Again!")
    case "cheese":
        if Jonessize == "small":
            Jonesprice = 399
        elif Jonessize == "medium":
            Jonesprice = 600
        elif Jonessize == "large":
            Jonesprice = 999
        else:
            print("Invalid size")
            print("Please Try Again!")
    case "veggie":
        if Jonessize == "small":
            Jonesprice = 450
        elif Jonessize == "medium":
            Jonesprice = 700
        elif Jonessize == "large":
            Jonesprice = 1100
        else:
            print("Invalid size")
            print("Please Try Again!")
    case "white":
        if Jonessize == "small":
            Jonesprice = 480
        elif Jonessize == "medium":
            Jonesprice = 720
        elif Jonessize == "large":
            Jonesprice = 1800
        else:
            print("Invalid size")
            print("Please Try Again!")
    case "watermelon":
        if Jonessize == "small":
            Jonesprice = 500
        elif Jonessize == "medium":
            Jonesprice = 800
        elif Jonessize == "large":
            Jonesprice = 1500
        else:
            print("Invalid size")
            print("Please Try Again!")
    case _:
        print("Invalid Pizza Flavor")

if Jonesprice > 0:
    print(f"{Jonesflavor.capitalize()} Pizza")
    print(f"Price: {Jonesprice}")
    print("Thank you for Purchasing")
    print("======================")

