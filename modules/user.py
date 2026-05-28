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

        self.db["users"][i] = {

            "name": name,

            "email": email,

            "phone": phone,

            "address": address,

            "age": age,

            "role": role,

            "membership": {

                "type": membership,

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
        if user_id in self.db["users"]:
            user = self.db["users"][user_id]
            print("Leave Blank To Keep Old Value\n")

             # NAME
            name = input(f"Name ({user['name']}): ")
            if name is None :
                return
            if name:
              user["name"] = self.validate_text("Name")

             # EMAIL
            email = input(f"Email ({user['email']}): ")
            if email is None:
                return
            if email:
                user["email"] = self.validate_email()

            # PHONE
            phone = input(f"Phone ({user['phone']}): ")
            if phone is None:
                return  
            if phone:
                user["phone"] = self.validate_phone()

            # ADDRESS
            address = input(f"Address ({user['address']}): ")
            if address is None:
                return
            if address:
                user["address"] = self.validate_text("Address")

            # AGE
            age = input(f"Age ({user['age']}): ")
            if age is None:
                return
            if age:
                user["age"] = self.validate_age()

            # ROLE
            role = input(f"Role ({user['role']}): ")
            if role is None:
                return
            if role:
                user["role"] = self.validate_text("Role")

            print("User Updated Successfully")

        else:
            print("User Not Found")

    # search user
    def search_user(self):
        i = input("Enter user ID to search: ")
        if i.lower() == "return":
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
        if user_id.lower() == "return":
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