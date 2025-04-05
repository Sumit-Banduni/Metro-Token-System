print("\t\t\t1. ADD STUDENT: ")
print("\t\t\t2. DELET STUDENT: ")
print("\t\t\t3. UPDATE STUDENT: ")
print("\t\t\t4. SEARCH STUDENT: ")
print("\t\t\t5. EXIT: ")

num = int(input("Enter your choice: "))
if num == 1:
    print("ADD STUDENT")
    name = input("Enter name: ")
    rollno = int(input("Enter rollno: "))
    marks = int(input("Enter marks: "))
    with open("school.csv", "a") as f:
        f.write(f"{name},{rollno},{marks}\n")
elif num == 2:
    print("DELETE STUDENT")
    rollno = int(input("Enter rollno: "))
    with open("school.csv", "r") as f:
        data = f.readlines()
    with open("school.csv", "w") as f:
        for line in data:
            if str(rollno) not in line:
                f.write(line)
elif num == 3:
    print("UPDATE STUDENT")
    rollno = int(input("Enter rollno: "))
    new_marks = int(input("Enter new marks: "))
    with open("school.csv", "r") as f:
        data = f.readlines()
    with open("school.csv", "w") as f:
        for line in data:
            if str(rollno) in line:
                f.write(f"{line.split(',')[0]},{line.split(',')[1]},{new_marks}\n")
            else:
                f.write(line)
elif num == 4:
    print("SEARCH STUDENT")
    rollno = int(input("Enter rollno: "))
    with open("school.csv", "r") as f:
        data = f.readlines()
    for line in data:
        if str(rollno) in line:
            print(line)
            break
    else:
        print("Student not found")
elif num == 5:
    print("EXIT")
else:
    print("Invalid choice")

        
        
