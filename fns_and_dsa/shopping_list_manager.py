# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item to add: ").strip()
            if item:  # Check if item is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item cannot be empty. Please try again.")
                
        elif choice == '2':
            # Remove an item from the shopping list
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
            else:
                print("Current shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                
                item_to_remove = input("Enter the item name to remove: ").strip()
                if item_to_remove in shopping_list:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' has been removed from your shopping list.")
                else:
                    print(f"'{item_to_remove}' was not found in your shopping list.")
                    
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nYour Shopping List:")
                print("-" * 20)
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("-" * 20)
                
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
