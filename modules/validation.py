
from database.database import Library


class Validation(Library):


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
            )

            if membership.strip().lower() == "return":
                return None

            if membership in memberships:

                return membership

            print("Invalid Membership Type!")
            
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
                return number
            print(f"Invalid {field}!")
            
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
                year, month, day = map(int, date.split("-"))
                if 1 <= year <= 2100:
                    if 1 <= month <= 12 and 1 <= day <= 31:
                        return date
                print("Invalid Date! Year must be between 0001 and 2100.")
            except ValueError:
                print(f"Invalid {field}! Must be in YYYY-MM-DD format.")
            
            
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
            
            
    def check_return(value):
        return value.strip().lower() == "return"
     
     
    #  # validate the user id        
    # def validate_user_id(self):
    #     while True:
    #         user_id = input("Enter User ID: ")
    #         if user_id in self.db["users"] and self.db["users"][user_id]["user_status"] == "active":
    #             return user_id
    #         print("Invalid User ID! Must be an existing active user ID.")
    
    
    # # validate book id
    # def validate_book_id(self):
    #     while True:
    #         book_id = input("Enter Book ID: ")
    #         if book_id in self.db["books"]:
    #             return book_id
    #         print("Invalid Book ID! Must be an existing book ID.")