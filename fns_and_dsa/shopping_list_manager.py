# shopping_list_manager.py

def display_menu():
    print("\n1. Add Item\n2. Remove Item\n3. View List\n4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Choice: ")
        
        if choice == '1':
            item = input("Add: ")
            if item:
                shopping_list.append(item)
                print(f"Added: {item}")
                
        elif choice == '2':
            if shopping_list:
                item = input("Remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"Removed: {item}")
                else:
                    print("Not found")
            else:
                print("List empty")
                
        elif choice == '3':
            if shopping_list:
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("List empty")
                
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
