def display_menu():
    print("\n\t\tDelhi Metro Routes")
    print("\t1. Red Line")
    print("\t2. Yellow Line")
    print("\t3. Blue Line")
    print("\t4. Green Line")
    print("\t5. Violet Line")
    print("\t6. Magenta Line")
    print("\t7. Pink Line")
    print("\t8. Exit\n")

def display_line(line_name, stations):
    print(f"\n{line_name}")
    print("-" * len(line_name))
    for station in stations:
        print(station)

def main():
    metro_routes = {
        "Red Line": [
            "Rithala", "Rohini West", "Rohini East", "Pitampura", "Kohat Enclave",
            "Netaji Subhash Place", "Keshav Puram", "Kanhaiya Nagar", "Inderlok",
            "Shastri Nagar", "Pratap Nagar", "Pulbangash", "Tis Hazari",
            "Kashmere Gate", "Shastri Park", "Seelampur", "Welcome", "Shahdara",
            "Mansarovar Park", "Jhilmil", "Dilshad Garden", "Shaheed Sthal"
        ],
        "Yellow Line": [
            "Samaypur Badli", "Rohini Sector 18, 19", "Haiderpur Badli Mor",
            "Jahangirpuri", "Adarsh Nagar", "Azadpur", "Model Town",
            "GTB Nagar", "Vishwavidyalaya", "Vidhan Sabha", "Civil Lines",
            "Kashmere Gate", "Chandni Chowk", "Chawri Bazar", "New Delhi",
            "Rajiv Chowk", "Patel Chowk", "Central Secretariat", "Udyog Bhawan",
            "Lok Kalyan Marg", "Jor Bagh", "INA", "AIIMS", "Green Park",
            "Hauz Khas", "Malviya Nagar", "Saket", "Qutab Minar", "Chhatarpur",
            "Sultanpur", "Ghitorni", "Arjan Garh", "Guru Dronacharya",
            "Sikanderpur", "MG Road", "IFFCO Chowk", "HUDA City Centre"
        ],
        "Blue Line": [
            "Dwarka Sector 21", "Dwarka Sector 8", "Dwarka Sector 9", 
            "Dwarka Sector 10", "Dwarka Sector 11", "Dwarka Sector 12", 
            "Dwarka Sector 13", "Dwarka Sector 14", "Dwarka", "Janakpuri West",
            "Janakpuri East", "Tilak Nagar", "Subhash Nagar", "Tagore Garden",
            "Rajouri Garden", "Ramesh Nagar", "Moti Nagar", "Kirti Nagar",
            "Shadipur", "Patel Nagar", "Rajendra Place", "Karol Bagh", 
            "Jhandewalan", "RK Ashram Marg", "Rajiv Chowk", "Barakhamba Road",
            "Mandi House", "Pragati Maidan", "Indraprastha", "Yamuna Bank",
            "Akshardham", "Mayur Vihar Phase-1", "Mayur Vihar Ext.",
            "New Ashok Nagar", "Noida Sector 15", "Noida Sector 16", 
            "Noida Sector 18", "Botanical Garden", "Noida City Centre", 
            "Noida Electronic City"
        ],
        "Green Line": [
            "Inderlok", "Ashok Park Main", "Satguru Ram Singh Marg", 
            "Punjabi Bagh West", "Shivaji Park", "Madipur", "Paschim Vihar East",
            "Paschim Vihar West", "Peera Garhi", "Udyog Nagar", "Surajmal Stadium",
            "Nangloi", "Nangloi Railway Station", "Rajdhani Park", "Mundka",
            "Mundka Industrial Area", "Ghevra", "Tikri Kalan", "Tikri Border",
            "Pandit Shree Ram Sharma", "Bahadurgarh City", "Brigadier Hoshiyar Singh"
        ],
        "Violet Line": [
            "Kashmere Gate", "Lal Quila", "Jama Masjid", "Delhi Gate", 
            "ITO", "Mandi House", "Janpath", "Central Secretariat", "Khan Market",
            "JLN Stadium", "Jangpura", "Lajpat Nagar", "Moolchand", "Kailash Colony",
            "Nehru Place", "Kalkaji Mandir", "Govind Puri", "Harkesh Nagar Okhla",
            "Jasola Apollo", "Sarita Vihar", "Mohan Estate", "Tughlakabad", 
            "Badarpur Border", "Sarai", "NHPC Chowk", "Mewala Maharajpur",
            "Sector 28", "Badkhal Mor", "Raja Nahar Singh"
        ],
        "Magenta Line": [
            "Botanical Garden", "Okhla Bird Sanctuary", "Kalindi Kunj", 
            "Jasola Vihar Shaheen Bagh", "Okhla Vihar", "Jamia Millia Islamia", 
            "Sukhdev Vihar", "NSIC Okhla", "Kalkaji Mandir", "Nehru Enclave",
            "Greater Kailash", "Chirag Delhi", "Panchsheel Park", "Hauz Khas",
            "IIT Delhi", "RK Puram", "Munirka", "Vasant Vihar", "Shankar Vihar",
            "IGI Airport Terminal 1", "Sadar Bazaar Cantonment", "Palam", 
            "Janakpuri West"
        ],
        "Pink Line": [
            "Majlis Park", "Azadpur", "Shalimar Bagh", "Netaji Subhash Place",
            "Shakurpur", "Punjabi Bagh West", "ESI Hospital", "Rajouri Garden",
            "Maya Puri", "Naraina Vihar", "Delhi Cantt.", "Durgabai Deshmukh South Campus",
            "INA", "Sarojini Nagar", "Bhikaji Cama Place", "RK Puram", "Munirka",
            "IIT Delhi", "Hauz Khas", "Chirag Delhi", "Greater Kailash",
            "Nehru Enclave", "Kalkaji Mandir", "Okhla NSIC", "Okhla Vihar",
            "Jamia Millia Islamia", "Jasola Vihar Shaheen Bagh", "Kalindi Kunj",
            "Botanical Garden"
        ]
    }

    while True:
        display_menu()
        choice = input("Select a line (1-8): ")
        if choice == "1":
            display_line("Red Line", metro_routes["Red Line"])
        elif choice == "2":
            display_line("Yellow Line", metro_routes["Yellow Line"])
        elif choice == "3":
            display_line("Blue Line", metro_routes["Blue Line"])
        elif choice == "4":
            display_line("Green Line", metro_routes["Green Line"])
        elif choice == "5":
            display_line("Violet Line", metro_routes["Violet Line"])
        elif choice == "6":
            display_line("Magenta Line", metro_routes["Magenta Line"])
        elif choice == "7":
            display_line("Pink Line", metro_routes["Pink Line"])
        elif choice == "8":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
