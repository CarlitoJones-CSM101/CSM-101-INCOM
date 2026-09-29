classrecord = {
    "Jones": {"StudID": "S001", "Grade": [90,85,86,82,83,90,92]},
    "Jeremy":{
        "StudID": "S002", "Grade": [72, 75, 59, 80, 84, 75, 85]
    },
    "Liza":{
        "studID": "S003",
        "Grade": [90, 87, 86, 84, 83, 93, 84]
    }
}
search_name = input("Enter the Student Name: ").title()
if search_name in classrecord:
    print(f"\nStudent {search_name} was Found!")

    student_id = classrecord[search_name]["StudID"]
    grades = classrecord[search_name]["Grade"]


    average = sum(grades) / len(grades)
    highest_grade = max(grades)
    lowest_grade = min(grades)


    intervention_status = "Normal"
    for grade in grades:
        if grade <= 60:
            intervention_status = " Candidate for intervention"
            break
print(f"Name: {search_name}")
print(f"ID: {student_id}")
print(f"Grades: {grades}")
print(f"Average Grade: {average:.2f}")
print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")
print(f"Status: {intervention_status}")