import json
import os

# In-memory storage for SAT results
sat_results = []

# File to store data in JSON format
DATA_FILE = "sat_results.json"

# Load data from JSON file if it exists
def load_data():
    global sat_results
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                sat_results = json.load(file)
        except json.JSONDecodeError:
            print("Error reading JSON file. Starting with empty data.")
            sat_results = []

# Save data to JSON file
def save_data():
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(sat_results, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

# Insert new SAT result
def insert_data():
    name = input("Enter Name: ").strip()
    # Check if name already exists
    if any(result['name'] == name for result in sat_results):
        print("Error: Name already exists. Please use a unique name.")
        return
    
    address = input("Enter Address: ").strip()
    city = input("Enter City: ").strip()
    country = input("Enter Country: ").strip()
    pincode = input("Enter Pincode: ").strip()
    
    # Validate SAT score
    while True:
        try:
            sat_score = float(input("Enter SAT Score (0-100): "))
            if 0 <= sat_score <= 100:
                break
            else:
                print("SAT Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Calculate pass/fail status
    passed = "Pass" if sat_score > 30 else "Fail"
    
    # Create result dictionary
    result = {
        "name": name,
        "address": address,
        "city": city,
        "country": country,
        "pincode": pincode,
        "sat_score": sat_score,
        "passed": passed
    }
    
    sat_results.append(result)
    save_data()
    print("Data inserted successfully!")

# View all data in JSON format
def view_all_data():
    if not sat_results:
        print("No data available.")
        return
    print(json.dumps(sat_results, indent=4))

# Get rank based on SAT score
def get_rank():
    name = input("Enter Name: ").strip()
    # Sort results by SAT score in descending order
    sorted_results = sorted(sat_results, key=lambda x: x['sat_score'], reverse=True)
    
    for i, result in enumerate(sorted_results, 1):
        if result['name'] == name:
            print(f"Rank of {name}: {i}")
            return
    print(f"No record found for {name}")

# Update SAT score
def update_score():
    name = input("Enter Name: ").strip()
    for result in sat_results:
        if result['name'] == name:
            while True:
                try:
                    new_score = float(input("Enter new SAT Score (0-100): "))
                    if 0 <= new_score <= 100:
                        result['sat_score'] = new_score
                        result['passed'] = "Pass" if new_score > 30 else "Fail"
                        save_data()
                        print("Score updated successfully!")
                        return
                    else:
                        print("SAT Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
    print(f"No record found for {name}")

# Delete a record
def delete_record():
    name = input("Enter Name: ").strip()
    global sat_results
    initial_length = len(sat_results)
    sat_results = [result for result in sat_results if result['name'] != name]
    if len(sat_results) < initial_length:
        save_data()
        print(f"Record for {name} deleted successfully!")
    else:
        print(f"No record found for {name}")

# Calculate average SAT score
def calculate_average_score():
    if not sat_results:
        print("No data available.")
        return
    total_score = sum(result['sat_score'] for result in sat_results)
    average = total_score / len(sat_results)
    print(f"Average SAT Score: {average:.2f}")

# Filter records by pass/fail status
def filter_by_status():
    status = input("Enter status to filter (Pass/Fail): ").strip().capitalize()
    if status not in ["Pass", "Fail"]:
        print("Invalid status. Please enter 'Pass' or 'Fail'.")
        return
    filtered_results = [result for result in sat_results if result['passed'] == status]
    if not filtered_results:
        print(f"No records found with {status} status.")
    else:
        print(json.dumps(filtered_results, indent=4))

# Main menu
def main():
    load_data()
    while True:
        print("\nSAT Results Management System")
        print("1. Insert Data")
        print("2. View All Data")
        print("3. Get Rank")
        print("4. Update Score")
        print("5. Delete One Record")
        print("6. Calculate Average SAT Score")
        print("7. Filter Records by Pass/Fail Status")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            insert_data()
        elif choice == "2":
            view_all_data()
        elif choice == "3":
            get_rank()
        elif choice == "4":
            update_score()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            calculate_average_score()
        elif choice == "7":
            filter_by_status()
        elif choice == "8":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()