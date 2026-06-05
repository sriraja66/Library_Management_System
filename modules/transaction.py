from datetime import datetime, timedelta
from modules.validation import Validation
class TransactionModule(Validation):
    def get_user_membership_setting(self, user_id, setting, default=None):
        membership_type = self.db["users"][user_id].get("membership", {}).get("type")
        return self.db["settings"]["memberships"].get(
            membership_type, {}
        ).get(setting, default)

    def issue_book(self):
        librarian_id = input("Enter librarian ID: ")
        if librarian_id.strip().lower() == "return":
            return
        if librarian_id in self.db["users"] and self.db["users"][librarian_id]["role"] == "librarian":
            user_id = self.select_user_id()
            if user_id is None:
                return
            if user_id in self.db["users"] and self.db["users"][user_id]["user_status"] == "active":
                book_id = input("Enter book ID: ")
                if book_id.strip().lower() == "return":
                    return

                # Duplicate check 
                for v in self.db["users"][user_id]["Transactions"].values():
                    if v["book_id"] == book_id and v["return_date"] is None:
                        print("This user has already issued this book and has not returned it yet.")
                        return

                # Membership and age restriction check
                book_info = self.db["books"].get(book_id)   
                if not book_info:
                    print("Book not found.")
                    return
                
                age_restriction = book_info["restrictions"]["age_restriction"]
                membership_restriction = book_info["restrictions"]["membership_restriction"]
                user_age = int(self.db["users"][user_id]["age"])
                
                if age_restriction and user_age < int(age_restriction):
                    print("User is not old enough to borrow this book.")
                    return
                user_membership = self.db["users"][user_id].get("membership", {}).get("type")
                if membership_restriction and user_membership != membership_restriction:
                    print("User does not meet the membership requirements for this book.")
                    return
                    
                # Check the reservation queue for the book
                if self.db["books"][book_id]["reservation_queue"]:
                    if self.db["books"][book_id]["reservation_queue"][0] != user_id:
                        print("This book is reserved for another user. You cannot borrow it at this time.")
                        return
                    else:
                        # Remove the user from the reservation queue
                        self.db["books"][book_id]["reservation_queue"].pop(0)
                
                # Create transaction
                if book_id in self.db["books"]:
                    if self.db["books"][book_id]["inventory"]["available_copies"] > 0:
                        
                        # Loop until a valid date format is given
                        while True:
                            issue_date_str = self.validate_date("issue date")
                            try:
                                if issue_date_str is None:
                                    return
                                issue_date_obj = datetime.strptime(issue_date_str, "%Y-%m-%d")
                                break
                            except ValueError:
                                print("Invalid date format. Please try again.")
                        
                        days = self.get_user_membership_setting(
                            user_id,
                            "max_reservation_days",
                            7
                        )
                        due_date_obj = issue_date_obj + timedelta(days=int(days))
                        
                        self.db["books"][book_id]["inventory"]["available_copies"] -= 1
                        
                        # Generate unique transaction ID string (e.g., "T1", "T2")
                        new_trans_id = f"T{len(self.db['users'][user_id]['Transactions']) + 1}"
                        
                        # Store transaction under its unique ID key
                        self.db["users"][user_id]["Transactions"][new_trans_id] = {
                            "transaction_id": new_trans_id,
                            "book_id": book_id,
                            "issued_by": librarian_id,
                            "issue_date": issue_date_obj.strftime("%Y-%m-%d"),
                            "due_date": due_date_obj.strftime("%Y-%m-%d"),
                            "return_date": None,
                            "status": "issued",
                            "fine": 0
                        }
                        
                        print(f"Book {book_id} issued to user {user_id} by librarian {librarian_id} successfully.")
                    else:
                        print("No copies available for this book.")
                else:
                    print("Book not found.")
            else:
                print("User not found or inactive.")
        else:
            print("Access denied. Invalid librarian ID or unauthorized role.")

    # Damage book 
    def damage_book(self):
        librarian_id = input("Enter librarian ID: ")
        if librarian_id.strip().lower() == "return":
            return
        user_id = input("Enter user ID: ")
        if user_id.strip().lower() == "return":
            return
        book_id = input("Enter book ID: ")
        if book_id.strip().lower() == "return":
            return
        if librarian_id in self.db["users"] and self.db["users"][librarian_id]["role"] == "librarian":
            if user_id in self.db["users"] and self.db["users"][user_id]["user_status"] == "active":
                if book_id in self.db["books"]:
                    while True:
                        date_str = self.validate_date("date")
                        if date_str is None:
                            return
                        try:
                            datetime.strptime(date_str, "%Y-%m-%d")
                            break
                        except ValueError:
                            print("Invalid date format. Please try again.")

                    self.db["users"][user_id]["history"][f"H{len(self.db['users'][user_id]['history']) + 1}"] = {
                        "book_id": book_id,
                        "action": "marked as damaged",
                        "date": date_str
                    }
                    self.db["books"][book_id]["inventory"]["damaged_copies"] += 1
                    print(f"Book {book_id} marked as damaged by librarian {librarian_id} for user {user_id}.")
                else:
                    print("Book not found.")
            else:
                print("User not found.") 
        else:
            print("Access denied. Invalid librarian ID or unauthorized role.")
    
    # Lost book 
    def lost_book(self):
        librarian_id = input("Enter librarian ID: ")
        if librarian_id.strip().lower() == "return":
            return
        user_id = input("Enter user ID: ")
        if user_id.strip().lower() == "return":
            return 
        book_id = input("Enter book ID: ")
        if book_id.strip().lower() == "return":
            return
        if librarian_id in self.db["users"] and self.db["users"][librarian_id]["role"] == "librarian":
            if user_id in self.db["users"] and self.db["users"][user_id]["user_status"] == "active":
                if book_id in self.db["books"]:
                    inventory = self.db["books"][book_id]["inventory"]
                    if inventory["available_copies"] <= 0:
                        print("No available copies to mark as lost.")
                        return
                    
                    while True:
                        date_str = self.validate_date("date")
                        if date_str is None:
                            return
                        try:
                            datetime.strptime(date_str, "%Y-%m-%d")
                            break
                        except ValueError:
                            print("Invalid date format. Please try again.")

                    self.db["users"][user_id]["history"][f"H{len(self.db['users'][user_id]['history']) + 1}"] = {
                        "book_id": book_id,
                        "action": "marked as lost",
                        "date": date_str
                    }
                    inventory["lost_copies"] += 1
                    inventory["available_copies"] -= 1
                    print(f"Book {book_id} marked as lost by librarian {librarian_id} for user {user_id}.")
                else:
                    print("Book not found.")
            else:
                print("User not found.") 
        else:
            print("Access denied. Invalid librarian ID or unauthorized role.")

    # Return book 
    def return_book(self):
        librarian_id = input("Enter librarian ID: ")
        if librarian_id.strip().lower() == "return":
            return
        if librarian_id in self.db["users"] and self.db["users"][librarian_id]["role"] == "librarian":
            user_id = input("Enter user ID: ")
            if user_id.strip().lower() =="return":
                return
            if user_id in self.db["users"] and self.db["users"][user_id]["user_status"] == "active":
                book_id = input("Enter book ID: ")
                if book_id.strip().lower() == "return":
                    return
                if book_id in self.db["books"]:
                    
                    while True:
                        return_date_str = self.validate_date("return date")
                        if return_date_str is None:
                            return
                        try:
                            return_date = datetime.strptime(return_date_str, "%Y-%m-%d")
                            break
                        except ValueError:
                            print("Invalid date format. Please try again.")
                    
                    transaction_found = False
                    for transaction_info in self.db["users"][user_id]["Transactions"].values():
                        if transaction_info["book_id"] == book_id and transaction_info["return_date"] is None:
                            
                            # Check late status securely using the verified active transaction record
                            due_date = datetime.strptime(transaction_info["due_date"], "%Y-%m-%d")
                            transaction_info["return_date"] = return_date_str
                            transaction_info["status"] = "returned"
                            self.db["books"][book_id]["inventory"]["available_copies"] += 1
                            if return_date > due_date:
                                print("Book is returned late. Calculate fine from Fine Management.")
                            print(f"Book {book_id} returned by user {user_id} to librarian {librarian_id} successfully.")
                            transaction_found = True
                            return
                    
                    if not transaction_found:
                        print("No active transaction found for this book and user.")
                else:
                    print("Book not found.")
            else:
                print("User not found.")
        else:
            print("Access denied. Invalid librarian ID or unauthorized role.")

    # View transactions
    def view_transactions(self):
        if not self.db["users"] or all(user["user_status"] != "active" for user in self.db["users"].values()):
            print("No users found.")
            return
        for user_id, user_info in self.db["users"].items():
            print(f"\nUser ID: {user_id}")
            if not user_info.get("Transactions"):
                print("  No transactions.")
                continue
            for transaction_id, transaction_info in user_info["Transactions"].items():
                print(f"  Transaction ID: {transaction_id}")
                for key, value in transaction_info.items():
                    print(f"    {key}: {value}")

    # Search transactions by user ID
    def search_transactions_by_user(self):
        user_id = input("Enter user ID to search transactions: ")
        if user_id.strip().lower() == "return":
            return
        if user_id in self.db["users"] and self.db["users"][user_id]["user_status"] == "active":
            print(f"\nUser ID: {user_id}")
            if not self.db["users"][user_id].get("Transactions"):
                print("  No transactions found for this user.")
                return
            for transaction_id, transaction_info in self.db["users"][user_id]["Transactions"].items():
                print(f"  Transaction ID: {transaction_id}")
                for key, value in transaction_info.items():
                    print(f"    {key}: {value}")
        else:
            print("User not found.")

    # Cancel transaction
    def cancel_transaction(self):
        librarian_id = input("Enter librarian ID: ")
        if librarian_id.strip().lower() == "return":
            return
        user_id = input("Enter user ID: ")
        if user_id.strip().lower() == "return":
            return
        book_id = input("Enter book ID: ")
        if book_id.strip().lower() == "return":
            return
        if librarian_id in self.db["users"] and self.db["users"][librarian_id]["role"] == "librarian":
            if user_id in self.db["users"] and self.db["users"][user_id]["user_status"] == "active":
                if book_id in self.db["books"]:
                    for transaction_info in self.db["users"][user_id]["Transactions"].values():
                        if transaction_info["book_id"] == book_id and transaction_info["return_date"] is None:
                            transaction_info["status"] = "cancelled"
                            transaction_info["return_date"] = "cancelled"
                            self.db["books"][book_id]["inventory"]["available_copies"] += 1
                            print(f"Transaction for book {book_id} cancelled by librarian {librarian_id} for user {user_id}.")
                            return
                    print("No active transaction found for this book and user.")
                else:
                    print("Book not found.")
            else:
                print("User not found.")
        else:
            print("Access denied. Invalid librarian ID or unauthorized role.")

    # Overdue transactions
    def view_overdue_transactions(self):
        today = datetime.today().date()
        overdue_found = False
        
        for user_id, user_info in self.db["users"].items():
            for transaction_id, transaction_info in user_info.get("Transactions", {}).items():
                if transaction_info["status"] == "issued":
                    due_date = datetime.strptime(transaction_info["due_date"], "%Y-%m-%d").date()
                    if due_date < today:
                        overdue_found = True
                        print(f"\nOverdue Transaction ID: {transaction_id} for User ID: {user_id}")
                        for key, value in transaction_info.items():
                            print(f"  {key}: {value}")
                            
        if not overdue_found:
            print("No overdue transactions found.")
    
    # transaction history by book ID
    def transaction_history_by_book(self):
        book_id = input("Enter book ID to view transaction history: ")
        if book_id.strip().lower() == "return":
            return
        if book_id in self.db["books"]:
            print(f"\nTransaction History for Book ID: {book_id}")
            history_found = False
            for user_id, user_info in self.db["users"].items():
                for transaction_id, transaction_info in user_info.get("Transactions", {}).items():
                    if transaction_info["book_id"] == book_id:
                        history_found = True
                        print(f"  Transaction ID: {transaction_id}, User ID: {user_id}")
                        for key, value in transaction_info.items():
                            print(f"    {key}: {value}")
            if not history_found:
                print("No transactions found for this book.")
        else:
            print("Book not found.")
