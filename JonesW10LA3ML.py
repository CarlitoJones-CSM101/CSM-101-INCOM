available_heroes = [
    "Aamon", "Akai", "Aldous", "Alice", "Alpha", "Alucard",
    "Angela", "Argus", "Arlott", "Atlas", "Aulus", "Aurora",
    "Badang", "Balmond", "Bane", "Barats", "Baxia", "Beatrix",
    "Belerick", "Benedetta", "Brody", "Bruno", "Carmilla",
    "Cecilion", "Chang'e", "Chip", "Chou", "Cici", "Claude",
    "Clint", "Cyclops", "Diggie", "Dyrroth", "Edith",
    "Esmeralda", "Estes", "Eudora", "Fanny", "Faramis",
    "Floryn", "Franco", "Fredrinn", "Freya", "Gatotkaca",
    "Gloo", "Gord", "Granger", "Grock", "Guinevere", "Gusion",
    "Hanabi", "Hanzo", "Harith", "Harley", "Hayabusa", "Helcurt",
    "Hilda", "Hirara", "Hylos", "Irithel", "Ixia", "Jawhead",
    "Johnson", "Joy", "Julian", "Kadita", "Kagura", "Kaja",
    "Kalea", "Karina", "Karrie", "Khaleed", "Khufra", "Kimmy",
    "Lancelot", "Lapu-Lapu", "Layla", "Leomord", "Lesley",
    "Ling", "Lolita", "Lukas", "Lunox", "Luo Yi", "Lylia",
    "Marcel", "Martis", "Masha", "Mathilda", "Melissa",
    "Minotaur", "Minsitthar", "Miya", "Moskov", "Nana",
    "Natalia", "Natan", "Nolan", "Novaria", "Obsidia", "Odette",
    "Paquito", "Pharsa", "Phoveus", "Popol and Kupa", "Rafaela",
    "Roger", "Ruby", "Saber", "Selena", "Silvanna", "Sora",
    "Sun", "Suyou", "Terizla", "Thamuz", "Tigreal", "Uranus",
    "Vale", "Valentina", "Valir", "Vexana", "Wanwan", "X.Borg",
    "Xavier", "Yi Sun-shin", "Yin", "Yu Zhong", "Yve", "Zetian",
    "Zhask", "Zhuxin", "Zilong"
]
while True:
    hero = input("Enter a Mobile Legends hero: ")

    found = False

    for available_hero in available_heroes:
        if available_hero.lower() == hero.lower():
            found = True
            break

    if found:
        print(hero.capitalize() + " is an available hero!")
    else:
        print(hero.capitalize() + " is not an available hero!")

    again = input("Would you like to check another hero? (y/n): ")

    if again.upper() != "Y":
        break