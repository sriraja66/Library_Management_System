from database.database import Library
from modules.validation import Validation
class User_module (Validation):


    # add user

    def add_user(self):

        i = f"U{len(self.db['users']) + 1}"

        name = self.validate_text("Name")

        if name is None:
            return

        email = self.validate_email()

        if email is None:
            return

        phone = self.validate_phone()

        if phone is None:
            return

        address = self.validate_text("Address")

        if address is None:
            return

        age = self.validate_age()

        if age is None:
            return

        role = self.validate_role()

        if role is None:
            return

        membership = self.validate_membership(
            self.db['settings']['memberships']
        )

        if membership is None:
            return

        user_details = {
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
            "age": age,
            "role": role,
            "membership": membership
        }

        user_validators = {
            "name": ("validate_text", "Name"),
            "email": "validate_email",
            "phone": "validate_phone",
            "address": ("validate_text", "Address"),
            "age": "validate_age",
            "role": "validate_role",
            "membership": ("validate_membership", self.db['settings']['memberships'])
        }

        if self.review_and_edit_details(user_details, user_validators, "User Details"):
            self.db["users"][i] = {

                "name": user_details["name"],

                "email": user_details["email"],

                "phone": user_details["phone"],

                "address": user_details["address"],

                "age": user_details["age"],

                "role": user_details["role"],

                "membership": {

                    "type": user_details["membership"],

                    "status": "active"
                },

                "Transactions": {},

                "Fines": {},

                "reservations": {},

                "reviews": {},

                "history": {},

                "user_status": "active"
            }

            print(f"User {i} added successfully.")

    # view all users

    def view_users(self):
        if not self.db["users"]:
            print("No users found.")
            return
        for user_id, user_info in self.db["users"].items():
            print(f"User ID: {user_id}")
            for key, value in user_info.items():
                print(f"{key}: {value}")
            print("\n")

    # update user details
    def update_user(self):
        user_id = input("Enter User ID: ")
        if user_id.strip().lower() == "return":
            return

        if user_id in self.db["users"]:
            user = self.db["users"][user_id]
            print("Leave Blank To Keep Old Value\n")

             # NAME
            name = input(f"Name ({user['name']}): ")
            if name.strip().lower() == "return":
                return
            if name:
              new_name = self.validate_text("Name")
              if new_name is None:
                  return
              user["name"] = new_name

             # EMAIL
            email = input(f"Email ({user['email']}): ")
            if email.strip().lower() == "return":
                return
            if email:
                new_email = self.validate_email()
                if new_email is None:
                    return
                user["email"] = new_email

            # PHONE
            phone = input(f"Phone ({user['phone']}): ")
            if phone.strip().lower() == "return":
                return
            if phone:
                new_phone = self.validate_phone()
                if new_phone is None:
                    return
                user["phone"] = new_phone

            # ADDRESS
            address = input(f"Address ({user['address']}): ")
            if address.strip().lower() == "return":
                return
            if address:
                new_address = self.validate_text("Address")
                if new_address is None:
                    return
                user["address"] = new_address

            # AGE
            age = input(f"Age ({user['age']}): ")
            if age.strip().lower() == "return":
                return
            if age:
                new_age = self.validate_age()
                if new_age is None:
                    return
                user["age"] = new_age

            # ROLE
            role = input(f"Role ({user['role']}): ")
            if role.strip().lower() == "return":
                return
            if role:
                new_role = self.validate_role()
                if new_role is None:
                    return
                user["role"] = new_role

            print("User Updated Successfully")

        else:
            print("User Not Found")

    # search user
    def search_user(self):
        i = input("Enter user ID to search: ")
        if self.is_return_input(i):
            return
        if i in self.db["users"]:
            print(f"User ID: {i}")
            for key, value in self.db["users"][i].items():
                print(f"{key}: {value}")
        else:
            print("User not found.")


    # delete user
    def delete_user(self):
        user_id = input("Enter user ID to delete: ")
        if self.is_return_input(user_id):
            return
        if user_id in self.db["users"]:
            self.db["users"][user_id]["user_status"] = "inactive"
            print(f"User {user_id} deleted successfully.")
        else:
            print("User not found.")


    # add the supplier details
    def add_supplier(self):
        i = f"S{len(self.db['suppliers']) + 1}"
        supplier_name = self.validate_text("supplier name")
        if supplier_name is None:
            return
        contact_info = self.validate_phone("contact number")
        if contact_info is None:
            return
        joining_date = self.validate_date("joining date")
        if joining_date is None:
            return
        address = self.validate_text("supplier address")
        if address is None:
            return

        self.db["suppliers"][i] = {
                "supplier_name": supplier_name,
                "contact_info": contact_info,
                "joining_date": joining_date,
                "address": address,
                "status": "active"
        }
        print(f"Supplier {i} added successfully.")
