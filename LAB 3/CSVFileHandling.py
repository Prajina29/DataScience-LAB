# 3. CSV File Handling
# ● Read data from a CSV file containing student records (roll number, name, marks)
# ● Display all student records
# ● Handle file-related and data conversion errors using try-except

import csv

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Roll", "Name", "Marks"])  
    writer.writerow([1, "Dipti", 85])
    writer.writerow([2, "Ram", 90])
    writer.writerow([3, "Sita", 78])
    writer.writerow([4, "Raju", "abc"]) 

    print("Roll", "Name", "Marks") 

try:
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  

        for row in reader:
            try:
                roll = int(row[0])
                name = row[1]
                marks = int(row[2])
                print(roll, name, marks)
            except ValueError:
                print("Invalid data:", row)

except FileNotFoundError:
    print("File not found")