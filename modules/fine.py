# add the fine module by seeing the user in fine module and then calculating the fine based on the number of days late and the fine per day.
import datetime

from modules.validation import Validation

class Fine_module(Validation):
    def calculate_fine(self):
        #check if user exists
        user_id = input("Enter User ID: ")
        if user_id.strip().lower() == "return":
            return
        current_date = self.validate_date("Enter current date (YYYY-MM-DD): ")
        if user_id not in self.db["users"] or self.db["users"][user_id]["user_status"] != "active":
            print("User Not Found or Inactive")
            return
        
        transactions = self.db["users"][user_id]["Transactions"]
        total_fine = 0
        for transaction in transactions.values():
            if transaction["status"] == "issued" and transaction["return_date"] is None:
                due_date = transaction["due_date"]
                fine_per_day = self.db["settings"]["fine_per_day"]
                days_late = (current_date - datetime.strptime(due_date, "%Y-%m-%d")).days
                
                if days_late > 0:
                    total_fine += days_late * fine_per_day
                    discount = self.db["users"][user_id]["membership"]["fine_discount"]
                    total_fine *= (1 - discount)
                    fines = self.db["users"][user_id]["fines"]
                    if "fines" not in fines:
                        fines["fines"] = []
                        fine_id = len(fines["fines"]) + 1   
                        fines["fines"].append({
                            "fine_id": fine_id,   
                            "book_id": transaction["book_id"],
                            "book_title": self.db["books"][transaction["book_id"]]["title"],
                            "amount": total_fine,
                            "date": current_date.strftime("%Y-%m-%d"),
                            "status": "unpaid"  })
                     
                else:
                    print(f"Transaction for book {transaction['book_id']} is not late.")
            else:
                print(f"Transaction for book {transaction['book_id']} is not currently issued or has already been returned.")
        print(f"Total Fine for User {user_id}: {total_fine}")
        
    # pay fine
        
    def pay_fine(self):
        user_id = input("Enter User ID: ")
        if user_id.strip().lower() == "return":
            return
        book_id = input("Enter Book ID: ")
        if book_id.strip().lower() == "return":
            return
        if user_id not in self.db["users"] or self.db["users"][user_id]["user_status"] != "active":
            print("User Not Found")
            return
        fines = self.db["users"][user_id]["fines"]
        if "fines" not in fines or not fines["fines"]:
            print("No fines found for this user.")
            return
        for fine in fines["fines"]:
            if fine["status"] == "unpaid" and fine["book_id"] == book_id:
                print(f"Fine ID: {fine['fine_id']}, Book ID: {fine['book_id']}, Amount: {fine['amount']}, Date: {fine['date']}")
        fine_id = int(input("Enter Fine ID to pay: "))
        for fine in fines["fines"]:
            if fine["fine_id"] == fine_id and fine["status"] == "unpaid":
                fine["status"] = "paid"
                print(f"Fine {fine_id} paid successfully.")
                return
        print("Fine not found or already paid.")
        
    # view All fines 
    def view_fines(self):
        user_id = input("Enter User ID: ")
        if user_id.strip().lower() == "return":
            return
        if user_id not in self.db["users"] or self.db["users"][user_id]["user_status"] != "active":
            print("User Not Found or Inactive")
            return
        fines = self.db["users"][user_id]["fines"]
        if "fines" not in fines or not fines["fines"]:
            print("No fines found for this user.")
            return
        for fine in fines["fines"]:
            print(f"Fine ID: {fine['fine_id']}, Book ID: {fine['book_id']}, Amount: {fine['amount']}, Date: {fine['date']}, Status: {fine['status']}")
        
    # view unpaid fines
    def view_unpaid_fines(self):    
        user_id = input("Enter User ID: ")
        if user_id.strip().lower() == "return":
            return
        if user_id not in self.db["users"]:
            print("User Not Found")
            return
        fines = self.db["users"][user_id]["fines"]
        if "fines" not in fines :
            print("No fines found for this user.")
            return
        for fine in fines["fines"]:
            if fine["status"] == "unpaid":
                print(f"Fine ID: {fine['fine_id']}, Book ID: {fine['book_id']}, Amount: {fine['amount']}, Date: {fine['date']}, Status: {fine['status']}")