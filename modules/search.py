from modules.validation import Validation


class SearchModule(Validation):
    def search_user_by_filters(self):
        name = input("Enter Name (or blank): ").strip().lower()
        email = input("Enter Email (or blank): ").strip().lower()
        phone = input("Enter Phone (or blank): ").strip()
        role = input("Enter Role (or blank): ").strip().lower()
        status = input("Enter Status (active/inactive or blank): ").strip().lower()

        found = False

        for user_id, user in self.db["users"].items():
            user_name = user["name"].lower()
            user_email = user["email"].lower()
            user_phone = user["phone"]
            user_role = user["role"].lower()
            user_status = user["user_status"].lower()

            if name and name not in user_name:
                continue
            if email and email not in user_email:
                continue
            if phone and phone != user_phone:
                continue
            if role and role != user_role:
                continue
            if status and status != user_status:
                continue

            print(f"User ID: {user_id}")
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Phone: {user['phone']}")
            print(f"Role: {user['role']}")
            print(f"Status: {user['user_status']}")
            print("-" * 30)
            found = True

        if not found:
            print("No matching users found.")

    def search_book_by_filters(self):
        title = input("Enter Title (or blank): ").strip().lower()
        author = input("Enter Author (or blank): ").strip().lower()
        genre = input("Enter Genre (or blank): ").strip().lower()
        available_only = input("Available only? (yes/no): ").strip().lower()

        found = False

        for book_id, book in self.db["books"].items():
            book_title = book["basic"]["title"].lower()
            book_author = book["basic"]["author"].lower()
            book_genre = book["basic"]["genre"].lower()
            available_copies = int(book["inventory"]["available_copies"])

            if title and title not in book_title:
                continue
            if author and author not in book_author:
                continue
            if genre and genre not in book_genre:
                continue
            if available_only == "yes" and available_copies <= 0:
                continue

            print(f"Book ID: {book_id}")
            print(f"Title: {book['basic']['title']}")
            print(f"Author: {book['basic']['author']}")
            print(f"Genre: {book['basic']['genre']}")
            print(f"Available Copies: {available_copies}")
            print("-" * 30)
            found = True

        if not found:
            print("No matching books found.")

