from datetime import datetime

from database.database import Library


class Validation(Library):

    def is_return_input(self, value):
        return value.strip().lower() == "return"


    # NAME + ADDRESS VALIDATION
    def validate_text(self, field):

        while True:

            value = input(
                f"Enter {field} "
                "(type 'return' to go back): "
            )

            if value.strip().lower() == "return":
                return None

            if value.replace(" ", "").isalpha():

                return value

            print(f"Invalid {field}!")

    def validate_email(self):

        while True:

            email = input(
                "Enter Email "
                "(type 'return' to go back): "
            )

            if email.strip().lower() == "return":
                return None

            if "@" in email and "." in email:
                return email

            print("Invalid Email!")

    # PHONE VALIDATION
    def validate_phone(self, field="Phone"):
        while True:
            phone = input(
                f"Enter {field} "
                "(type 'return' to go back): "
            )
            if phone.strip().lower() == "return":
                return None
            if phone.isdigit() and len(phone) == 10:
                return phone
            print("Invalid Phone Number!")


    # AGE VALIDATION
    def validate_age(self):
        while True:
            age = input(
                "Enter Age "
                "(type 'return' to go back): "
            )
            if age.strip().lower() == "return":
                return None
            try:
                age_int = int(age)
                if age_int > 0 and age_int < 120:
                    return age
                else:
                    print("Age Must Be A Number Between 1 And 119!")
            except:
                print("Age Must Be A Number!")

    # MEMBERSHIP VALIDATION
    def validate_membership(self, memberships):
        while True:
            print("\nAvailable Memberships:")

            for name, details in memberships.items():

                print(
                    f"\n{name.upper()}\n"
                    f"Book Limit: {details['book_limit']}\n"
                    f"Reservation Limit: "
                    f"{details['reservation_limit']}\n"
                    f"Fine Discount: "
                    f"{details['fine_discount']}\n"
                    f"Max Reservation Days: "
                    f"{details['max_reservation_days']}\n"
                    f"{'-' * 30}"
                )

            membership = input(
                "Enter Membership Type "
                "(type 'return' to go back): "
            ).strip().lower()

            if membership == "return":
                return None

            if membership in memberships:

                return membership

            print("Invalid Membership Type!")

    def validate_book_membership_restriction(self):
        while True:
            valid_memberships = self.db["settings"]["memberships"]
            print("\nAvailable Membership Restrictions:")
            for membership in valid_memberships:
                print(f"- {membership}")

            membership = input(
                "Enter Membership Restriction "
                "(type 'return' to go back): "
            ).strip().lower()

            if membership == "return":
                return None

            if membership in valid_memberships:
                return membership

            print("Invalid Membership Restriction! Enter basic or premium.")

    #isbn validation
    def validate_isbn(self):
        while True:
            isbn = input(
                "Enter ISBN "
                "(type 'return' to go back): "
            )
            if isbn.strip().lower() == "return":
                return None
            if len(isbn)  == 13 and isbn.isdigit():
                return isbn
            print("Invalid ISBN! must be a 13 digit number.")


    # publication year validation
    def validate_publication_year(self):
        while True:
            year = input(
                "Enter Publication Year "
                "(type 'return' to go back): "
            )
            if year.strip().lower() == "return":
                return None
            if len(year) == 4 and year.isdigit():
                return year
            print("Invalid Publication Year!")

    # number validation
    def validate_number(self, field):
        while True:
            number = input(
                f"Enter {field} "
                "(type 'return' to go back): "
            )
            if number.strip().lower() == "return":
                return None
            if number.isdigit():
                return int(number)
            print(f"Invalid {field}!")

    def validate_review_text(self):
        while True:
            review = input(
                "Enter review "
                "(type 'return' to go back): "
            ).strip()

            if review.lower() == "return":
                return None

            if review:
                return review

            print("Review cannot be empty.")

    # review rating validation
    def validate_rating(self):
        while True:
            rating = input(
                "Enter Rating (1-5) "
                "(type 'return' to go back): "
            )
            if rating.strip().lower() == "return":
                return None
            if rating.isdigit():
                rating_int = int(rating)
                if 1 <= rating_int <= 5:
                    return rating
            print("Invalid Rating! Must be a number between 1 and 5.")

    # date validation simple
    def validate_date(self, field):
        while True:
            date = input(
                f"Enter {field} (YYYY-MM-DD) "
                "(type 'return' to go back): "
            ).strip()
            if date.strip().lower() == "return":
                return None
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%d")
                if 1 <= parsed_date.year <= 2100:
                    return date
                print("Invalid Date! Year must be between 0001 and 2100.")
            except ValueError:
                print(
                    f"Invalid {field}! Enter a real date in YYYY-MM-DD format. "
                    "Example: 2026-06-03"
                )


    # role validation libibrarian, member , admin
    def validate_role(self):
        while True:
            role = input(
                "Enter Role (librarian/member/admin) "
                "(type 'return' to go back): "
            )
            if role.strip().lower() == "return":
                return None
            if role in ["librarian", "member", "admin"]:
                return role
            print("Invalid Role! Must be librarian, member, or admin.")

    # validate supplier id for book supplier details
    def validate_supplier_id(self):
        while True:
            supplier_id = input(
                "Enter Supplier ID "
                "(type 'return' to go back): "
            )
            if supplier_id.strip().lower() == "return":
                return None
            if supplier_id in self.db["suppliers"] and supplier_id.strip() != "":
                return supplier_id
            print("Invalid Supplier ID! Must be an existing supplier ID. and cannot be empty.")

    # validate supplier name for book supplier details
    def validate_supplier_name(self):
        while True:
            supplier_name = input(
                "Enter Supplier Name "
                "(type 'return' to go back): "
            )
            if supplier_name.strip().lower() == "return":
                return None
            if supplier_name in [supplier["supplier_name"] for supplier in self.db["suppliers"].values()] and supplier_name.strip() != "":  
                return supplier_name
            print("Invalid Supplier Name! Must be an existing supplier name. or cannot be empty.")

    # contact info validation for book supplier details
    def validate_contact_info(self):
        while True:
            contact_info = input(
                "Enter Supplier Contact Info "
                "(type 'return' to go back): "
            )
            if contact_info.strip().lower() == "return":
                return None
            if contact_info.isdigit() and len(contact_info) == 10 and contact_info in [supplier["contact_info"] for supplier in self.db["suppliers"].values()]:
                return contact_info
            print("Invalid Contact Info! Must be a 10 digit phone number. and must be an existing contact info in suppliers.")


    def check_return(self, value):
        return self.is_return_input(value)


    # validate the user id
    def validate_user_id(self):
        while True:
            user_id = input("Enter User ID: ")
            if self.is_return_input(user_id):
                return None
            if (
                user_id in self.db["users"]
                and self.db["users"][user_id]["user_status"] == "active"
            ):
                return user_id
            print("Invalid User ID! Must be an existing active user ID.")

    def ask_to_add_user(self):
        choice = input(
            "User not found. Do you want to add user now? (yes/no): "
        ).strip().lower()

        if choice == "yes":
            self.add_user()
            return True

        print("User not added.")
        return False

    def select_user_id(self):
        while True:
            user_id = input("Enter User ID: ")

            if self.is_return_input(user_id):
                return None

            if (
                user_id in self.db["users"]
                and self.db["users"][user_id]["user_status"] == "active"
            ):
                return user_id

            added = self.ask_to_add_user()
            if added:
                print("Now enter the User ID again.")

    def validate_book_id(self):
        while True:
            book_id = input("Enter Book ID: ")
            if self.is_return_input(book_id):
                return None
            if book_id in self.db["books"]:
                return book_id
            print("Invalid Book ID! Must be an existing book ID.")

    def confirm_details(self, data, title="Review Details"):
        print(f"\n===== {title} =====")
        for key, value in data.items():
            print(f"{key.replace('_', ' ').capitalize()}: {value}")
        
        confirm = input("\nPress Enter to Confirm or type 'cancel' to discard: ").strip().lower()
        if confirm == 'cancel':
            print("Operation Cancelled.")
            return False
        return True

    def review_and_edit_details(self, data, validators, title="Review Details"):
        while True:
            fields = list(data.keys())
            print(f"\n===== {title} =====")
            for index, key in enumerate(fields, start=1):
                label = key.replace("_", " ").capitalize()
                print(f"{index}. {label}: {data[key]}")

            choice = input(
                "\nPress Enter to save, type field number/name to edit, "
                "or type 'cancel' to discard: "
            ).strip()

            if choice == "":
                return True

            if choice.lower() == "cancel":
                print("Operation Cancelled.")
                return False

            selected_key = None
            if choice.isdigit():
                selected_index = int(choice) - 1
                if 0 <= selected_index < len(fields):
                    selected_key = fields[selected_index]
            else:
                normalized_choice = choice.lower().replace(" ", "_")
                for key in fields:
                    if key.lower() == normalized_choice:
                        selected_key = key
                        break

            if selected_key is None or selected_key not in validators:
                print("Invalid field. Please choose a valid field number or name.")
                continue

            validator = validators[selected_key]

            if isinstance(validator, str):
                new_value = getattr(self, validator)()
            else:
                method_name = validator[0]
                args = validator[1:]
                new_value = getattr(self, method_name)(*args)

            if new_value is None:
                print("Edit cancelled. Keeping old value.")
                continue

            data[selected_key] = new_value
