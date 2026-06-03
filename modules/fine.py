# add the fine module by seeing the user in fine module and then calculating the fine based on the number of days late and the fine per day.
import datetime

from modules.validation import Validation

class Fine_module(Validation):
    def get_user_fines(self, user_id):
        return self.db["users"][user_id].setdefault("Fines", {})

    def get_fine_discount(self, user_id):
        membership = self.db["users"][user_id].get("membership", {})
        if "fine_discount" in membership:
            return membership["fine_discount"]
        membership_type = membership.get("type")
        return self.db["settings"]["memberships"].get(
            membership_type, {}
        ).get("fine_discount", 0)

    def calculate_fine(self):
        #check if user exists
        user_id = input("Enter User ID: ")
        if user_id.strip().lower() == "return":
            return
        current_date = self.validate_date("current date")
        if current_date is None:
            return
        if user_id not in self.db["users"] or self.db["users"][user_id]["user_status"] != "active":
            print("User Not Found or Inactive")
            return
        
        transactions = self.db["users"][user_id]["Transactions"]
        new_fine_total = 0
        fines = self.get_user_fines(user_id)
        fines.setdefault("fines", [])
        discount = self.get_fine_discount(user_id)

        for transaction_id, transaction in transactions.items():
            if transaction["status"] == "issued" and transaction["return_date"] is None:
                calculation_date = current_date
            elif transaction["status"] == "returned" and transaction["return_date"]:
                calculation_date = transaction["return_date"]
            else:
                print(f"Transaction for book {transaction['book_id']} is not currently issued or returned late.")
                continue

            due_date = transaction["due_date"]
            fine_per_day = self.db["settings"]["fine_per_day"]
            calculation_date_obj = datetime.datetime.strptime(calculation_date, "%Y-%m-%d")
            due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d")
            days_late = (calculation_date_obj - due_date_obj).days
                
            if days_late > 0:
                fine_amount = days_late * fine_per_day * (1 - discount)

                already_unpaid = any(
                    fine.get("transaction_id") == transaction_id
                    and fine["status"] == "unpaid"
                    for fine in fines["fines"]
                )
                if not already_unpaid:
                    new_fine_total += fine_amount
                    fine_id = len(fines["fines"]) + 1
                    fines["fines"].append({
                        "fine_id": fine_id,
                        "transaction_id": transaction_id,
                        "book_id": transaction["book_id"],
                        "book_title": self.db["books"][transaction["book_id"]]["basic"]["title"],
                        "amount": fine_amount,
                        "date": calculation_date,
                        "status": "unpaid"
                    })
            else:
                print(f"Transaction for book {transaction['book_id']} is not late.")
        print(f"New Fine for User {user_id}: {new_fine_total}")
        
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
        fines = self.get_user_fines(user_id)
        if "fines" not in fines or not fines["fines"]:
            print("No fines found for this user.")
            return
        for fine in fines["fines"]:
            if fine["status"] == "unpaid" and fine["book_id"] == book_id:
                print(f"Fine ID: {fine['fine_id']}, Book ID: {fine['book_id']}, Amount: {fine['amount']}, Date: {fine['date']}")
        fine_id_input = input("Enter Fine ID to pay: ")
        if fine_id_input.strip().lower() == "return":
            return
        if not fine_id_input.isdigit():
            print("Invalid Fine ID")
            return
        fine_id = int(fine_id_input)
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
        fines = self.get_user_fines(user_id)
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
        fines = self.get_user_fines(user_id)
        if "fines" not in fines :
            print("No fines found for this user.")
            return
        for fine in fines["fines"]:
            if fine["status"] == "unpaid":
                print(f"Fine ID: {fine['fine_id']}, Book ID: {fine['book_id']}, Amount: {fine['amount']}, Date: {fine['date']}, Status: {fine['status']}")
