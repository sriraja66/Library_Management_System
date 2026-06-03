import os

from modules.transaction import TransactionModule
from modules.books import Books_module
from modules.reservation import Reservation_module
from modules.fine import Fine_module
from modules.user import User_module
from modules.review import ReviewModule
from modules.search import SearchModule


class LibraryManagementSystem(
    TransactionModule,
    Books_module,
    Reservation_module,
    Fine_module,
    User_module,
    ReviewModule,
    SearchModule
):
    pass


lms = LibraryManagementSystem()


def main_help():
    os.system("cls")
    print("\n===== MAIN MENU HELP =====\n")
    print("1. User Management")
    print("   Add, view, update, search, and delete users.")
    print("2. Book Management")
    print("   Add, view, update, search, delete, and check books.")
    print("3. Transaction Management")
    print("   Issue books, return books, and view transactions.")
    print("4. Fine Management")
    print("   Calculate, pay, and view fines.")
    print("5. Reservation Management")
    print("   Reserve books, cancel reservations, and search reservations.")
    print("6. Review Management")
    print("   Add reviews, view reviews, and search reviews.")
    print("7. Search")
    print("   Search users and books by ID or filters.")
    print("8. Exit")
    print("   Close the program.")
    print("\nType 'return' to go back or exit from input fields.")
    input("\nPress Enter To Continue...")


def user_help():
    os.system("cls")
    print("\n===== USER MANAGEMENT HELP =====\n")
    print("1. Add User - Register a new user.")
    print("2. View User - Show all users.")
    print("3. Update User - Change user details.")
    print("4. Search User - Find a user by user ID.")
    print("5. Delete User - Mark a user as inactive.")
    print("6. Back - Return to main menu.")
    print("\nDuring update, leave blank to keep old value.")
    print("Type 'return' to go back.")
    input("\nPress Enter To Continue...")


def book_help():
    os.system("cls")
    print("\n===== BOOK MANAGEMENT HELP =====\n")
    print("1. Add Book - Add a new book.")
    print("2. View Books - Show all books.")
    print("3. Update Book - Change book details.")
    print("4. Search Books - Find a book by book ID.")
    print("5. Delete Book - Remove a book.")
    print("6. Check Availability - See available copies.")
    print("7. Add Supplier - Add supplier details for new books.")
    print("8. Back - Return to main menu.")
    print("\nType 'return' to go back.")
    input("\nPress Enter To Continue...")


def transaction_help():
    os.system("cls")
    print("\n===== TRANSACTION MANAGEMENT HELP =====\n")
    print("1. Issue Book - Give a book to a user.")
    print("2. Return Book - Mark an issued book as returned.")
    print("3. View Transactions - Show all transactions.")
    print("4. Search Transactions - Search transactions by user ID.")
    print("5. Back - Return to main menu.")
    print("\nOnly librarian users can issue or return books.")
    print("Type 'return' to go back.")
    input("\nPress Enter To Continue...")


def fine_help():
    os.system("cls")
    print("\n===== FINE MANAGEMENT HELP =====\n")
    print("1. Calculate Fine - Calculate fine for late books.")
    print("2. Pay Fine - Mark a fine as paid.")
    print("3. View Fines - Show user fines.")
    print("4. Back - Return to main menu.")
    print("\nType 'return' to go back.")
    input("\nPress Enter To Continue...")


def reservation_help():
    os.system("cls")
    print("\n===== RESERVATION MANAGEMENT HELP =====\n")
    print("1. Reserve Book - Reserve a book for a user.")
    print("2. Cancel Reservation - Cancel a user reservation.")
    print("3. View Reservations - Show all reservations.")
    print("4. Search Reservations by User - Find reservations for a user.")
    print("5. Search Reservations by Book - Find reservations for a book.")
    print("6. Back - Return to main menu.")
    print("\nType 'return' to go back.")
    input("\nPress Enter To Continue...")


def review_help():
    os.system("cls")
    print("\n===== REVIEW MANAGEMENT HELP =====\n")
    print("1. Review Book - Add a review and rating for a book.")
    print("2. View Reviews - Show reviews for a book.")
    print("3. Search Reviews by User - Show reviews written by a user.")
    print("4. Back - Return to main menu.")
    print("\nRating must be from 1 to 5.")
    print("Type 'return' to go back.")
    input("\nPress Enter To Continue...")


def search_help():
    os.system("cls")
    print("\n===== SEARCH MENU HELP =====\n")
    print("1. Search User by ID - Find one user by exact ID.")
    print("2. Search User by Filters - Find users by name, email, phone, role, or status.")
    print("3. Search Book by ID - Find one book by exact ID.")
    print("4. Search Book by Filters - Find books by title, author, genre, or availability.")
    print("5. Search Transaction by User ID - View transactions for one user.")
    print("6. Search Reservation by User ID - View reservations for one user.")
    print("7. Search Fine by User ID - View fines for one user.")
    print("8. Search Review by User ID - View reviews written by one user.")
    print("9. Back - Return to main menu.")
    print("\nType 'return' to go back.")
    input("\nPress Enter To Continue...")


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
        print("Type help for menu help")

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
            break

        elif choice.strip().lower() == "help":
            user_help()
            continue
        
        elif choice.strip().lower() == "return":
            return

        else:
            print("Invalid Choice")
        
       

        continue_choice = input("\nPress Enter To Continue...")
        if continue_choice.strip().lower() == "return":
            return


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
        print("7. Add Supplier")
        print("8. Back")
        print("Type help for menu help")

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
            lms.add_supplier()

        elif choice == "8":
            break

        elif choice.strip().lower() == "help":
            book_help()
            continue
        
       
        elif choice.strip().lower() == "return":
            return

        else:
            print("Invalid Choice")

        continue_choice = input("\nPress Enter To Continue...")
        if continue_choice.strip().lower() == "return":
            return

def transaction_menu():
    while True:
        os.system("cls")

        print("\n===== TRANSACTION MANAGEMENT =====\n")

        print("1. Issue Book")
        print("2. Return Book")
        print("3. View Transactions")
        print("4. Search Transactions")
        print("5. Back")
        print("Type help for menu help")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            lms.issue_book()

        elif choice == "2":
            lms.return_book()

        elif choice == "3":
            lms.view_transactions()

        elif choice == "4":
            lms.search_transactions_by_user()

        elif choice.strip().lower() == "help":
            transaction_help()
            continue
            
       
        elif choice.strip().lower() == "return":
            return

        elif choice == "5":
            break

        else:
            print("Invalid Choice")

        continue_choice = input("\nPress Enter To Continue...")
        if continue_choice.strip().lower() == "return":
            return
        
def fine_menu():
    while True:
        os.system("cls")

        print("\n===== FINE MANAGEMENT =====\n")

        print("1. Calculate Fine")
        print("2. Pay Fine")
        print("3. View Fines")
        print("4. Back")
        print("Type help for menu help")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            lms.calculate_fine()

        elif choice == "2":
            lms.pay_fine()

        elif choice == "3":
            lms.view_fines()

        elif choice == "4":
            break

        elif choice.strip().lower() == "help":
            fine_help()
            continue
        
     
        elif choice.strip().lower() == "return":
            return
        else:
            print("Invalid Choice")

        continue_choice = input("\nPress Enter To Continue...")
        if continue_choice.strip().lower() == "return":
            return

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
            print("Type help for menu help")

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

            elif choice.strip().lower() == "help":
                reservation_help()
                continue
            
            
            elif choice.strip().lower() == "return":
                 return

            else:
                print("Invalid Choice")

            continue_choice = input("\nPress Enter To Continue...")
            if continue_choice.strip().lower() == "return":
                return
    
    
def review_menu():
        while True:
            os.system("cls")

            print("\n===== REVIEW MANAGEMENT =====\n")

            print("1. Review Book")
            print("2. View Reviews")
            print("3. Search Reviews by User")
            print("4. Back")
            print("Type help for menu help")

            choice = input("\nEnter Choice: ")

            if choice == "1":
                lms.review_book()

            elif choice == "2":
                lms.view_reviews()

            elif choice == "3":
                lms.search_reviews_by_user()

            elif choice == "4":
                break

            elif choice.strip().lower() == "help":
                review_help()
                continue
            
            
            elif choice.strip().lower() == "return":
                return

            else:
                print("Invalid Choice")

            continue_choice = input("\nPress Enter To Continue...")
            if continue_choice.strip().lower() == "return":
                return


def search_menu():
        while True:
            os.system("cls")

            print("\n===== SEARCH MENU =====\n")

            print("1. Search User by ID")
            print("2. Search User by Filters")
            print("3. Search Book by ID")
            print("4. Search Book by Filters")
            print("5. Search Transaction by User ID")
            print("6. Search Reservation by User ID")
            print("7. Search Fine by User ID")
            print("8. Search Review by User ID")
            print("9. Back")
            print("Type help for menu help")

            choice = input("\nEnter Choice: ")

            if choice == "1":
                lms.search_user()

            elif choice == "2":
                lms.search_user_by_filters()

            elif choice == "3":
                lms.search_book()

            elif choice == "4":
                lms.search_book_by_filters()

            elif choice == "5":
                lms.search_transactions_by_user()

            elif choice == "6":
                lms.search_reservations_by_user()

            elif choice == "7":
                lms.view_fines()

            elif choice == "8":
                lms.search_reviews_by_user()

            elif choice == "9":
                break

            elif choice.strip().lower() == "help":
                search_help()
                continue

            elif choice.strip().lower() == "return":
                return

            else:
                print("Invalid Choice")

            continue_choice = input("\nPress Enter To Continue...")
            if continue_choice.strip().lower() == "return":
                return

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
    print("7. Search")
    print("8. Exit")
    print("Type help for menu help")

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
        search_menu()

    elif choice.strip().lower() == "help":
        main_help()
        continue

    elif choice.strip().lower() == "return":
        print("\nGoodbye!")
        break

    elif choice == "8":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid Choice")
        continue_choice = input("\nPress Enter To Continue...")
        if continue_choice.strip().lower() == "return":
            break
