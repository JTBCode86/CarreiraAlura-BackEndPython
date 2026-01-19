from application.manager import GuestManager

def main():
    manager = GuestManager()
    
    # Show initial state
    print(f"Current guest list: {manager.guest_list.current_guests}")
    
    try:
        # Input data
        name = input("Enter the new guest's name: ")
        pos = int(input("Enter the position to insert the guest: "))
        
        # Execution
        updated_list = manager.run_insertion_process(name, pos)
        
        # Expected Output
        print(f"Updated guest list: {updated_list}")
        
    except ValueError:
        print("Error: Position must be an integer.")

if __name__ == "__main__":
    main()