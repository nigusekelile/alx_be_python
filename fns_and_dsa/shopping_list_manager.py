# shopping_list_manager.py

# Implementation of an array (list) at module level so checks can find it
shopping_list = []

def display_menu():
    """Prints the main menu for the shopping list manager."""
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    global shopping_list  # use the top-level shopping_list
    while True:
        # Calling display_menu function
        display_menu()

        # Choice input as a number (int) with validation
        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:  # prevent empty input
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to your shopping list.")
            else:
                print("⚠️ Item cannot be empty.")
        
        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ '{item}' has been removed from your shopping list.")
            else:
                print(f"⚠️ '{item}' not found in the shopping list.")
        
        elif choice == 3:
            if shopping_list:
                print("\n🛒 Your current shopping list:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("🛒 Your shopping list is empty.")
        
        elif choice == 4:
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
