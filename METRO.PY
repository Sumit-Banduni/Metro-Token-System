import random
import os
import tkinter as tk
# Metro stations list
stations = [
    "Rithala", "Rohini West", "Rohini East", "Pitampura", "Kohat Enclave",
    "Netaji Subhash Place", "Keshav Puram", "Kanhaiya Nagar", "Inderlok",
    "Shastri Nagar", "Pratap Nagar", "Pulbangash", "Tis Hazari", "Kashmere Gate",
    "Shastri Park", "Seelampur", "Welcome", "Shahdara", "Mansarovar Park",
    "Jhilmil", "Dilshad Garden", "Escorts Mujesar", "Sant Surdas", "Raja Nahar Singh",
    "Ballabgarh", "Faridabad New Town", "Neelam Chowk Ajronda", "Bata Chowk"
]

def display_menu():
    print("\n\t\t\tMETRO TOKEN SYSTEM")
    print("\t\t\t1. BUY TOKEN")
    print("\t\t\t2. DELETE TOKEN")
    print("\t\t\t3. UPDATE TOKEN")
    print("\t\t\t4. SEARCH TOKEN")
    print("\t\t\t5. PRINT SLIP")
    print("\t\t\t6. EXIT\n")

def display_stations():
    print("\nAvailable Stations:")
    for i, station in enumerate(stations, start=1):
        print(f"{i}. {station}")

def calculate_price(source, destination):
    source_index = stations.index(source)
    destination_index = stations.index(destination)
    gap = abs(destination_index - source_index)
    if 1 <= gap <= 2:
        return 10
    elif 3 <= gap <= 5:
        return 20
    elif 6 <= gap <= 8:
        return 30
    elif 9 <= gap <= 11:
        return 40
    elif 12 <= gap <= 14:
        return 50
    elif 15 <= gap <= 28:
        return 60
    return 0

def buy_token():
    display_stations()
    source = input("\nEnter source station: ").strip()
    destination = input("Enter destination station: ").strip()
    
    if source in stations and destination in stations:
        price = calculate_price(source, destination)
        if price == 0:
            print("Error calculating price. Please try again.")
            return
        token = random.randint(1000, 9999)
        print(f"\nTicket price from {source} to {destination}: {price}")
        print(f"Your token number is: {token}")

        # Save the token to a file
        with open("metro.csv", "a") as f:
            f.write(f"{token},{source},{destination},{price}\n")
    else:
        print("Invalid station names. Please try again.")

def delete_token():
    token = input("\nEnter the token number to delete: ").strip()
    if not os.path.exists("metro.csv"):
        print("No tokens found.")
        return

    with open("metro.csv", "r") as f:
        lines = f.readlines()

    with open("metro.csv", "w") as f:
        found = False
        for line in lines:
            if line.startswith(token):
                found = True
            else:
                f.write(line)

    if found:
        print(f"Token {token} has been deleted.")
    else:
        print(f"Token {token} not found.")

def update_token():
    token = input("\nEnter the token number to update: ").strip()
    new_token = input("Enter the new token number: ").strip()
    if not os.path.exists("metro.csv"):
        print("No tokens found.")
        return

    with open("metro.csv", "r") as f:
        lines = f.readlines()

    with open("metro.csv", "w") as f:
        found = False
        for line in lines:
            if line.startswith(token):
                parts = line.strip().split(",")
                parts[0] = new_token
                f.write(",".join(parts) + "\n")
                found = True
            else:
                f.write(line)

    if found:
        print(f"Token {token} has been updated to {new_token}.")
    else:
        print(f"Token {token} not found.")

def search_token():
    token = input("\nEnter the token number to search: ").strip()
    if not os.path.exists("metro.csv"):
        print("No tokens found.")
        return

    with open("metro.csv", "r") as f:
        for line in f:
            if line.startswith(token):
                print(f"Token found: {line.strip()}")
                return

    print(f"Token {token} not found.")

def print_slip():
    token = input("\nEnter the token number to print slip: ").strip()
    if not os.path.exists("metro.csv"):
        print("No tokens found.")
        return

    with open("metro.csv", "r") as f:
        for line in f:
            if line.startswith(token):
                details = line.strip().split(",")
                print("\n============================")
                print("        METRO RECEIPT")
                print("============================")
                print(f"Token Number: {details[0]}")
                print(f"From: {details[1]}")
                print(f"To: {details[2]}")
                print(f"Fare: {details[3]}")
                print("============================\n")
                return

    print(f"Token {token} not found.")

# Main loop
while True:
    display_menu()
    try:
        choice = int(input("Enter your choice: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue

    if choice == 1:
        buy_token()
    elif choice == 2:
        delete_token()
    elif choice == 3:
        update_token()
    elif choice == 4:
        search_token()
    elif choice == 5:
        print_slip()
    elif choice == 6:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")

