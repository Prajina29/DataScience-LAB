# 3. Student Marks Manager
# Store student names as keys and marks (list of integers) as values in a dictionary. Compute
# each student’s average and grade (A/B/C/D). Print the top 2 students based on average marks.

def Student_Marks_Manager():
    
    print("Enter Student name and marks like- Prajina:99,Dipti:98,Joker:29")
   
    while True:
        user_input = input("Enter Student Name and Marks: ").strip() # strip le front ra back ko whitespace hataucha
        
        if user_input == "":
            print("No more input. Exiting...")
            break

    students = {}

    entries = user_input.split(",")

    for entry in entries:
        name, mark = entry.split(":")
        students[name] = [int(mark)]
    
    averages = {}

    print("\nStudent Results:")
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        averages[name] = avg

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "D"

        print(f"{name} → Average: {avg:.2f}, Grade: {grade}")
    
    sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)

    print("\nTop 2 Students:")
    for i in range(min(2, len(sorted_students))):
        print(f"{i+1}. {sorted_students[i][0]} → Average: {sorted_students[i][1]:.2f}")

Student_Marks_Manager()
