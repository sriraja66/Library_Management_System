from modules.validation import Validation
class Reservation_module( Validation):

    # reserve the book
    def reserve_book(self):
        user_id = input("Enter User ID: ")
        if self.is_return_input(user_id):
            return
        if user_id not in self.db["users"] or self.db["users"][user_id]["user_status"] != "active":
            print("User Not Found")
            return

        book_id = input("Enter Book ID: ")
        if self.is_return_input(book_id):
            return
        if book_id not in self.db["books"]:
            print("Book Not Found")
            return
        user = self.db["users"][user_id]
        book = self.db["books"][book_id]

        # membership status check
        if user["membership"]["status"] == "inactive":
            print("User Membership Is Inactive")
            return

        # restriction checks
        age_restriction = book["restrictions"].get("age_restriction")
        membership_restriction = book["restrictions"].get("membership_restriction")
        user_age = int(user["age"])
        # age restriction
        if age_restriction and user_age < int(age_restriction):
            print("User Is Not Old Enough")
            return
        # membership restriction
        if (
            membership_restriction
            and user["membership"]["type"] != membership_restriction
        ):
            print("Membership Requirement Not Met")
            return
        # duplicate reservation check
        for reservation in user["reservations"].values():

            if (
                reservation["book_id"] == book_id
                and reservation["status"] == "reserved"
            ):
                print("Book Already Reserved")
                return
        
        reservation_date = self.validate_date("Reservation Date (YYYY-MM-DD)")
        if reservation_date is None:
            return

        reservation_details = {
            "user": user["name"],
            "book": book["basic"]["title"],
            "date": reservation_date
        }

        if self.confirm_details(reservation_details, "Reservation Details"):
            # add to reservation queue
            book["reservation_queue"].append(user_id)
            # create reservation
            reservation_id = f"R{len(user['reservations']) + 1}"
            user["reservations"][reservation_id] = {
                "book_id": book_id,
                "reservation_date": reservation_date,
                "status": "reserved",
            }
            print(f"Book {book_id} Reserved " f"For User {user_id}")


    # cancel reservation by user
    def cancel_reservation(self):
        user_id = input("Enter User ID: ")
        if self.is_return_input(user_id):
            return
        if user_id not in self.db["users"] or self.db["users"][user_id]["user_status"] != "active":
            print("User Not Found or Inactive")
            return
        book_id = input("Enter Book ID: ")
        if self.is_return_input(book_id):
            return
        if book_id not in self.db["books"]:
            print("Book Not Found")
            return
        user = self.db["users"][user_id]
        book = self.db["books"][book_id]
        reservation_key = None
        # find reservation
        for key, reservation in user["reservations"].items():
            if (
                reservation["book_id"] == book_id
                and reservation["status"] == "reserved"
            ):
                reservation_key = key
                break
        if reservation_key is None:
            print("Reservation Not Found")
            return
        # remove from queue
        if user_id in book["reservation_queue"]:
            book["reservation_queue"].remove(user_id)
        # delete reservation
        del user["reservations"][reservation_key]
        print("Reservation Cancelled Successfully")


    # cancel reservation by librarian
    def cancel_reservation_by_librarian(self):
        book_id = input("Enter Book ID: ")
        if self.is_return_input(book_id):
            return

        if book_id not in self.db["books"]:
            print("Book Not Found")
            return
        book = self.db["books"][book_id]
        queue = book["reservation_queue"]
        if not queue:
            print("No Reservation Queue")
            return
        print("Current Queue:", queue)
        remove_users_input = input("Enter User IDs To Remove " "(comma separated): ")
        if self.is_return_input(remove_users_input):
            return
        remove_users = remove_users_input.split("," )
        # remove spaces
        cleaned_users = []
        for user in remove_users:
            cleaned_users.append(user.strip())
        remove_users = cleaned_users
        # update queue
        new_queue = []
        for user in queue:
            if user not in remove_users:
                new_queue.append(user)
        book["reservation_queue"] = new_queue
        # remove reservations
        for user_id in remove_users:
            if user_id not in self.db["users"]:
                continue
            reservations = self.db["users"][user_id]["reservations"]
            remove_keys = []
            for key, value in reservations.items():
                if value["book_id"] == book_id and value["status"] == "reserved":
                    remove_keys.append(key)
            # delete reservations
            for key in remove_keys:
                del reservations[key]
        print("Reservations Cancelled Successfully")


    # view  reservations
    def view_reservations(self):
        if not self.db["users"]:
            print("No users found.")
            return
        for user_id, user_info in self.db["users"].items():
            print(f"User ID: {user_id}")
            for reservation_id, reservation_info in user_info["reservations"].items():
                print(f"Reservation ID: {reservation_id}")
                for key, value in reservation_info.items():
                    print(f"{key}: {value}")


    # search reservations by user ID
    def search_reservations_by_user(self):
        user_id = input("Enter user ID to search reservations: ")
        if self.is_return_input(user_id):
            return
        if user_id in self.db["users"] and self.db["users"][user_id]["user_status"] == "active":
            print(f"User ID: {user_id}")
            for reservation_id, reservation_info in self.db["users"][user_id]["reservations"].items():
                print(f"Reservation ID: {reservation_id}")
                for key, value in reservation_info.items():
                    print(f"{key}: {value}")
        else:
            print("User not found.")

    # search reservations by book ID
    def search_reservations_by_book(self):
        book_id = input("Enter book ID to search reservations: ")
        if self.is_return_input(book_id):
            return
        if book_id in self.db["books"]:
            print(f"Book ID: {book_id}")
            for user_id, user_info in self.db["users"].items():
                for reservation_id, reservation_info in user_info["reservations"].items():
                    if reservation_info["book_id"] == book_id:
                        print(f"User ID: {user_id}")
                        print(f"Reservation ID: {reservation_id}")
                        for key, value in reservation_info.items():
                            print(f"{key}: {value}")
        else:
            print("Book not found.")
