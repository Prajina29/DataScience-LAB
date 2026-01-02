# 5. Menu-Driven File Operations
# Write data to a file
# Read data from a file
# Append data to a file
# Handle invalid user input and file errors using exception handling

while True:
    print("\n1. rite to file")
    print("2. Read file")
    print("3. Append to file")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter text to write: ")
            with open("data.txt", "w") as f:
                f.write(data)
            print("Data written successfully")

        elif choice == 2:
            with open("data.txt", "r") as f:
                print("File content:")
                print(f.read())

        elif choice == 3:
            data = input("Enter text to append: ")
            with open("data.txt", "a") as f:
                f.write(data)
            print("Data appended successfully")

        elif choice == 4:
            print("Program exited")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a number")

    except FileNotFoundError:
        print("File not found") 
