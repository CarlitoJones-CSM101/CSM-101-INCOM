print("===================")
print("Grade Calculator")
print("====================")

jonesgrade = int(input("What is your Grade: "))

print("====Grades====")

print("Your Grade is:",jonesgrade)

match jonesgrade:
    case n if 90 <= n <= 100:
        jonesrating = "Excellent"
    case n if 80 <= n <= 89:
        jonesrating = "Very Good"
    case n if 75 <= n <= 79:
        jonesrating = "Passed"
    case n if 0 <= n <= 74:
        jonesrating = "Failed"
    case _:
        print("Invalid Grade")

print("Your Rating is:",jonesrating)
print("==================")

