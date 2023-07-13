import time

employee_data = {}

def add_employee():
    name = input ("\nEnter Employee Name: ")
    number = input ("\nEnter Employee Number: ")
    employee_data[name] = number
    
    print("\nEmployee Added Succecfully")
    time.sleep(5)
    
def search_employee():
    name = input ("\nEnter Employee Name to Search: ")
    if name in employee_data:
        print(f"\nEmployee found! name: \n{name}, \nEmployee Number: \n{employee_data[name]},")
        time.sleep(5)
    else:
        print("\n OOPS!! Employee not found")
        time.sleep(5)
        
def print_all_employees():
    print("-----Registered Employees: -----")
    if employee_data:
        for name, number in employee_data.items():
            print(f"\nName: {name}, Number: {number}")
            time.sleep(5)
    else:
        print("\n---No employees registered.---")
        time.sleep(5)
        
def animate_exit_message():
    message = "/././.Exiting the program./././"
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.3)
    print()
    time.sleep(2) 

def main():
    while True:
        print("\n1. Add Employee")
        print("\n2. Search Employee")
        print("\n3. Show all Employees")
        print("\n4. Quit")
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            search_employee()
        elif choice == "3":
            print_all_employees()
        elif choice == "4":
            animate_exit_message()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
    