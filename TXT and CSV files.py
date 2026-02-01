"""
Task 8: File Handling and CSV Operations in Python
"""

import csv

# ---------- TEXT FILE OPERATIONS ----------
try:
    # 1. Create text file & write user data
    with open("data.txt", "w") as file:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
    print("\nText file created and data written successfully.")

    # 2. Read file contents
    with open("data.txt", "r") as file:
        print("\nReading file contents:")
        print(file.read())

    # 3. Append data to file
    with open("data.txt", "a") as file:
        city = input("Enter your city: ")
        file.write(f"City: {city}\n")
    print("\nData appended successfully.")

    # 4. Read updated file
    with open("data.txt", "r") as file:
        print("\nUpdated file contents:")
        print(file.read())

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error occurred:", e)

# ---------- CSV FILE OPERATIONS ----------
try:
    # 5. Create CSV file & write multiple rows
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Marks"])
        writer.writerow([1, "Manasa", 85])
        writer.writerow([2, "Rahul", 90])
        writer.writerow([3, "Anita", 88])
    print("\nCSV file created and data written successfully.")

    # 6. Read CSV data
    print("\nReading CSV file data:")
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

except FileNotFoundError:
    print("CSV file not found.")
except Exception as e:
    print("Error occurred:", e)

print("\nAll file operations completed successfully.")
