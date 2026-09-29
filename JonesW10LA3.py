while True:
    print(f"{'':=^40}")
    print(f"{'|           GAME NAME CHECKER          |':^40}")
    print(f"{'':=^40}")

    game = input("Enter a game name: ")

    found = False

    for character in game:
        if character in "!@#$%0123456789":
            found = True
            break

    print(f"{'':=^40}")

    if found:
        print("Game name contains a special character!")
    else:
        print("Game name has no special character!")
    print(f"{'':=^40}")

    again = input("Would you like to try another game? (y/n): ")

    if again.upper() != "Y":
        break

print(f"{'':=^40}")
print(f"{'|            PROGRAM ENDED             |':^40}")
print(f"{'|         By: Carlito V. Jones         |':^40}")
print(f"{'':=^40}")



