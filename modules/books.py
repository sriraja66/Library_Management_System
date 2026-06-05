from database.database import Library
from modules.validation import Validation

class Books_module(Validation):
    #add book 

    def ask_to_add_supplier(self):
        choice = input(
            "Supplier not found. Do you want to add supplier now? (yes/no): "
        ).strip().lower()

        if choice == "yes":
            self.add_supplier()
            return True

        print("Supplier not added.")
        return False

    def select_supplier_id(self):
        while True:
            supplier_id = input(
                "Enter Supplier ID "
                "(type 'return' to go back): "
            )

            if self.is_return_input(supplier_id):
                return None

            if supplier_id in self.db["suppliers"]:
                return supplier_id

            added = self.ask_to_add_supplier()
            if added:
                print("Now enter the Supplier ID again.")

    def add_book(self):
        i = f"B{len(self.db['books']) + 1}"
        title = self.validate_text("title")
        if title is None:
            return
        author = self.validate_text("author")
        if author is None:
            return
        isbn = self.validate_isbn()
        if isbn is None:
            return
        publication_year = self.validate_publication_year()
        if publication_year is None:
            return
        genre = self.validate_text("genre")
        if genre is None:
            return
        main_category = self.validate_text("main category")
        if main_category is None:
            return
        sub_category = self.validate_text("sub category")
        if sub_category is None:
            return
        shelf = self.validate_number("shelf number")
        if shelf is None:
            return
        row = self.validate_number("row number")
        if row is None:
            return
        section = self.validate_text("section")
        if section is None:
            return
        total_copies = self.validate_number("total copies")
        if total_copies is None:
            return
        age_restriction = self.validate_number("age restriction")
        if age_restriction is None:
            return
        membership_restriction = self.validate_book_membership_restriction()
        if membership_restriction is None:
            return
        borrowing_limit = self.validate_number("borrowing limit")
        if borrowing_limit is None:
            return
        supplier_id = self.select_supplier_id()
        if supplier_id is None:
            return
        supplier = self.db["suppliers"][supplier_id]

        book_details = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "publication_year": publication_year,
            "genre": genre,
            "main_category": main_category,
            "sub_category": sub_category,
            "shelf": shelf,
            "row": row,
            "section": section,
            "total_copies": total_copies,
            "age_restriction": age_restriction,
            "membership_restriction": membership_restriction,
            "borrowing_limit": borrowing_limit,
            "supplier_id": supplier_id,
            "supplier_name": supplier["supplier_name"],
            "contact_info": supplier["contact_info"]
        }

        book_validators = {
            "title": ("validate_text", "title"),
            "author": ("validate_text", "author"),
            "isbn": "validate_isbn",
            "publication_year": "validate_publication_year",
            "genre": ("validate_text", "genre"),
            "main_category": ("validate_text", "main category"),
            "sub_category": ("validate_text", "sub category"),
            "shelf": ("validate_number", "shelf number"),
            "row": ("validate_number", "row number"),
            "section": ("validate_text", "section"),
            "total_copies": ("validate_number", "total copies"),
            "age_restriction": ("validate_number", "age restriction"),
            "membership_restriction": "validate_book_membership_restriction",
            "borrowing_limit": ("validate_number", "borrowing limit"),
            "supplier_id": "select_supplier_id"
        }

        if self.review_and_edit_details(book_details, book_validators, "Book Details"):
            supplier_id = book_details["supplier_id"]
            supplier = self.db["suppliers"][supplier_id]
            book_details["supplier_name"] = supplier["supplier_name"]
            book_details["contact_info"] = supplier["contact_info"]

            self.db["books"][i] = {
                "basic":
                {
                    "title": book_details["title"],
                    "author": book_details["author"],
                    "isbn": book_details["isbn"],
                    "publication_year": book_details["publication_year"],
                    "genre": book_details["genre"]
                },
                "category": {
                    "main_category": book_details["main_category"],
                    "sub_category": book_details["sub_category"]
                },
                "location": {
                    "shelf": book_details["shelf"],
                    "row": book_details["row"],
                    "section": book_details["section"]
            },
              "reservation_queue":[],

                "inventory": {
                    "total_copies": book_details["total_copies"],
                    "available_copies": book_details["total_copies"],
                    "damaged_copies": 0,
                    "lost_copies": 0
            },
                "restrictions": {
                    "age_restriction": book_details["age_restriction"],
                    "membership_restriction": book_details["membership_restriction"],
                    "borrowing_limit": book_details["borrowing_limit"]
            },
                "supplier": {

                    "supplier_id": book_details["supplier_id"],
                    "supplier_name": book_details["supplier_name"],
                    "contact_info": book_details["contact_info"]
                }
            }
            print(f"Book {i} added successfully.")

    # view books

    def view_books(self):
        if not self.db["books"]:
            print("No books found.")
            return
        for book_id, book_info in self.db["books"].items():
            print(f"Book ID: {book_id}")
            for key, value in book_info.items():
                print(f"{key}: {value}")

    # update book

    def update_book(self):
        book_id = input("Enter book ID to update: ")
        if self.is_return_input(book_id):
            return
        if book_id in self.db["books"]:
            book = self.db["books"][book_id]
            print("Leave Blank To Keep Old Value\n")

            # TITLE
            title = input(f"Title ({book['basic']['title']}): ")
            if self.is_return_input(title):
                return
            if title:
                new_title = self.validate_text("title")
                if new_title is None:
                    return
                book["basic"]["title"] = new_title

            # AUTHOR
            author = input(f"Author ({book['basic']['author']}): ")
            if self.is_return_input(author):
                return
            if author:
                new_author = self.validate_text("author")
                if new_author is None:
                    return
                book["basic"]["author"] = new_author

            # ISBN
            isbn = input(f"ISBN ({book['basic']['isbn']}): ")
            if self.is_return_input(isbn):
                return
            if isbn:
                new_isbn = self.validate_isbn()
                if new_isbn is None:
                    return
                book["basic"]["isbn"] = new_isbn

            # PUBLICATION YEAR
            publication_year = input(
                f"Publication Year ({book['basic']['publication_year']}): "
            )
            if self.is_return_input(publication_year):
                return
            if publication_year:
                new_publication_year = self.validate_publication_year()
                if new_publication_year is None:
                    return
                book["basic"]["publication_year"] = new_publication_year

            # GENRE
            genre = input(f"Genre ({book['basic']['genre']}): ")
            if self.is_return_input(genre):
                return
            if genre:
                new_genre = self.validate_text("genre")
                if new_genre is None:
                    return
                book["basic"]["genre"] = new_genre

            # age restriction
            age_restriction = input(
                f"Age Restriction ({book['restrictions']['age_restriction']}): "
            )
            if self.is_return_input(age_restriction):
                return
            if age_restriction:
                new_age_restriction = self.validate_number("age restriction")
                if new_age_restriction is None:
                    return
                book["restrictions"]["age_restriction"] = new_age_restriction

            # membership restriction
            membership_restriction = input(
                f"Membership Restriction ({book['restrictions']['membership_restriction']}): "
            )
            if self.is_return_input(membership_restriction):
                return
            if membership_restriction:
                new_membership_restriction = self.validate_book_membership_restriction()
                if new_membership_restriction is None:
                    return
                book["restrictions"]["membership_restriction"] = new_membership_restriction

            # borrowing limit
            borrowing_limit = input(
                f"Borrowing Limit ({book['restrictions']['borrowing_limit']}): "
            )
            if self.is_return_input(borrowing_limit):
                return
            if borrowing_limit:
                new_borrowing_limit = self.validate_number("borrowing limit")
                if new_borrowing_limit is None:
                    return
                book["restrictions"]["borrowing_limit"] = new_borrowing_limit

            # supplier name
            supplier_name = input(
                f"Supplier Name ({book['supplier']['supplier_name']}): "
            )
            if self.is_return_input(supplier_name):
                return
            if supplier_name:
                new_supplier_name = self.validate_text("supplier name")
                if new_supplier_name is None:
                    return
                book["supplier"]["supplier_name"] = new_supplier_name

            # supplier contact info
            contact_info = input(
                f"Supplier Contact Info ({book['supplier']['contact_info']}): "
            )
            if self.is_return_input(contact_info):
                return
            if contact_info:
                new_contact_info = self.validate_phone("supplier contact number")
                if new_contact_info is None:
                    return
                book["supplier"]["contact_info"] = new_contact_info

            # location
            shelf = input(
                f"Shelf Location ({book['location']['shelf']}): "
            )
            if self.is_return_input(shelf):
                return
            if shelf:
                new_shelf = self.validate_number("shelf location")
                if new_shelf is None:
                    return
                book["location"]["shelf"] = new_shelf
            # row
            row = input(
                f"Row Location ({book['location']['row']}): "
            )
            if self.is_return_input(row):
                return
            if row:
                new_row = self.validate_number("row location")
                if new_row is None:
                    return
                book["location"]["row"] = new_row

            # section
            section = input(
                f"Section Location ({book['location']['section']}): "
            )
            if self.is_return_input(section):
                return
            if section:
                new_section = self.validate_text("section location")
                if new_section is None:
                    return
                book["location"]["section"] = new_section

            print(f"Book {book_id} updated successfully.")

        else:
            print("Book not found.")

    # search book

    def search_book(self):
        i = input("Enter book ID to search: ")
        if self.is_return_input(i):
            return
        if i in self.db["books"]:
            print(f"Book ID: {i}")
            for key, value in self.db["books"][i].items():
                print(f"{key}: {value}")
        else:
            print("Book not found.")

    # delete book

    def delete_book(self):
        book_id = input("Enter book ID to delete: ")
        if self.is_return_input(book_id):
            return
        if book_id in self.db["books"]:
            confirm = input(f"Are you sure you want to delete {book_id}? (yes/no): ")
            if confirm.strip().lower() != "yes":
                print("Delete cancelled.")
                return
            del self.db["books"][book_id]
            print(f"Book {book_id} deleted successfully.")
        else:
            print("Book not found.")

    # check availability

    def check_availability(self):
        book_id = input("Enter book ID to check availability: ")
        if self.is_return_input(book_id):
            return
        if book_id in self.db["books"]:
            available_copies = self.db["books"][book_id]["inventory"]["available_copies"]
            print(f"Book {book_id} has {available_copies} copies available.")
        else:
            print("Book not found.")
