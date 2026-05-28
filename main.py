import os

from modules.transaction import TransactionModule
from modules.books import Books_module
from modules.reservation import Reservation_module
from modules.fine import Fine_module
from modules.user import User_module
from modules.review import ReviewModule


class LibraryManagementSystem(
    TransactionModule,
    Books_module,
    Reservation_module,
    Fine_module,
    User_module,
    ReviewModule
):
    pass


lms = LibraryManagementSystem()


#user menu
def user_menu():
    while True:
        os.system("cls")

        print("\n===== USER MANAGEMENT =====\n")

        print("1. Add User")
        print("2. View User")
        print("3. Update User")
        print("4. Search User")
        print("5. Delete User")
        print("6. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            lms.add_user()

        elif choice == "2":
            lms.view_users()

        elif choice == "3":
            lms.update_user()

        elif choice == "4":
            lms.search_user()

        elif choice == "5":
            lms.delete_user()
            
        elif choice == "6":
            lms.add_supplier()

        elif choice == "7":
            break
        
        elif choice.strip().lower() == "return":
            return

        else:
            print("Invalid Choice")
        
       

        input("\nPress Enter To Continue...")


# ================= BOOK MENU =================
def book_menu():
    while True:
        os.system("cls")

        print("\n===== BOOK MANAGEMENT =====\n")

        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Search Books")
        print("5. Delete Book")
        print("6. Check Availability")
        print("7. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            lms.add_book()

        elif choice == "2":
            lms.view_books()

        elif choice == "3":
            lms.update_book()

        elif choice == "4":
            lms.search_book()

        elif choice == "5":
            lms.delete_book()

        elif choice == "6":
            lms.check_availability()

        elif choice == "7":
            break
        
       
        elif choice.strip().lower() == "return":
            return

        else:
            print("Invalid Choice")

        input("\nPress Enter To Continue...")

def transaction_menu():
    while True:
        os.system("cls")

        print("\n===== TRANSACTION MANAGEMENT =====\n")

        print("1. Issue Book")
        print("2. Return Book")
        print("3. View Transactions")
        print("4. Search Transactions")
        print("5. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            lms.issue_book()

        elif choice == "2":
            lms.return_book()

        elif choice == "3":
            lms.view_transactions()

        elif choice == "4":
            lms.search_transactions_by_user()
            
       
        elif choice.strip().lower() == "return":
            return

        elif choice == "5":
            break

        else:
            print("Invalid Choice")

        input("\nPress Enter To Continue...")
        
def fine_menu():
    while True:
        os.system("cls")

        print("\n===== FINE MANAGEMENT =====\n")

        print("1. Calculate Fine")
        print("2. Pay Fine")
        print("3. View Fines")
        print("4. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            lms.calculate_fine()

        elif choice == "2":
            lms.pay_fine()

        elif choice == "3":
            lms.view_fines()

        elif choice == "4":
            break
        
     
        elif choice.strip().lower() == "return":
            return
        else:
            print("Invalid Choice")

        input("\nPress Enter To Continue...")

def reservation_menu():
        while True:
            os.system("cls")

            print("\n===== RESERVATION MANAGEMENT =====\n")

            print("1. Reserve Book")
            print("2. Cancel Reservation")
            print("3. View Reservations")
            print("4. Search Reservations by User")
            print("5. Search Reservations by Book")
            print("6. Back")

            choice = input("\nEnter Choice: ")

            if choice == "1":
                lms.reserve_book()

            elif choice == "2":
                lms.cancel_reservation()

            elif choice == "3":
                lms.view_reservations()

            elif choice == "4":
                lms.search_reservations_by_user()

            elif choice == "5":
                lms.search_reservations_by_book()

            elif choice == "6":
                break
            
            
            elif choice.strip().lower() == "return":
                 return

            else:
                print("Invalid Choice")

            input("\nPress Enter To Continue...")
    
    
def review_menu():
        while True:
            os.system("cls")

            print("\n===== REVIEW MANAGEMENT =====\n")

            print("1. Review Book")
            print("2. View Reviews")
            print("3. Search Reviews by User")
            print("4. Back")

            choice = input("\nEnter Choice: ")

            if choice == "1":
                lms.review_book()

            elif choice == "2":
                lms.view_reviews()

            elif choice == "3":
                lms.search_reviews_by_user()

            elif choice == "4":
                break
            
            
            elif choice.strip().lower() == "return":
                return

            else:
                print("Invalid Choice")

            input("\nPress Enter To Continue...")

# ================= MAIN MENU =================
while True:

    os.system("cls")

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====\n")

    print("1. User Management")
    print("2. Book Management")
    print("3. Transaction Management")
    print("4. Fine Management")
    print("5. Reservation Management")
    print("6. Review Management")
    print("7. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        user_menu()

    elif choice == "2":
        book_menu()
    
    elif choice == "3":
        transaction_menu()
        
    elif choice == "4":
        fine_menu()
        
    elif choice == "5":
        reservation_menu()
    
    elif choice == "6":
        review_menu()

    elif choice == "7":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid Choice")
        input("\nPress Enter To Continue...")