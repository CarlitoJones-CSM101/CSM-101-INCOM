# ASSIGNMENT PART 1
jones_patients = {
    "ana": (80, 50, 150, 90, 140,160,70),
    "ben": (130, 140, 135, 90, 140,150,180),
    "carlo": (90, 100, 95, 90, 140,80,140)
}

for jonespatient, jonesreadings in jones_patients.items():
    print("=====================")
    print("Patient:", jonespatient.capitalize())
    print("~~~~~~~~~~~~~~~~~~~~~")
    jones_high_count = 0

    print("=====================")
    print("Blood Sugar Summary")
    print("=====================")
    for jonesreading in jonesreadings:
        if jonesreading >= 120:
            jonesstatus = "High"
            jones_high_count += 1
        else:
            jonesstatus = "Normal"

        jones_max = max(jonesreadings)
        jones_min = min(jonesreadings)
        jones_avg = sum(jonesreadings) / len(jonesreadings)
        jones_diff = jones_max - jones_min

        print(jonesreading, "-", jonesstatus)
    print("=====================")
    print("\nNumber of High Readings:", jones_high_count)
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"\nHighest Blood Sugar: {jones_max:.0f}")
    print(f"\nLowest Blood Sugar: {jones_min:.0f}")
    print(f"\nAverage Blood Sugar: {jones_avg:.0f}")
    print(f"\nThe Difference in Blood Sugar: {jones_diff}")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")








