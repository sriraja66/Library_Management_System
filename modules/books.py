from database.database import Library
from modules.validation import Validation

class Books_module(Validation):
    #add book 

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
        copies_available = self.validate_number("copies available")
        if copies_available is None:
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
        available_copies = self.validate_number("available copies")
        if available_copies is None:
            return
        reserved_copies = self.validate_number("reserved copies")
        if reserved_copies is None:
            return
        damaged_copies = self.validate_number("damaged copies")
        if damaged_copies is None:
            return
        lost_copies = self.validate_number("lost copies")
        if lost_copies is None:
            return
        age_restriction = self.validate_number("age restriction")
        if age_restriction is None:
            return
        membership_restriction = self.validate_text("membership restriction")
        if membership_restriction is None:
            return
        borrowing_limit = self.validate_number("borrowing limit")
        if borrowing_limit is None:
            return
        supplier_id = self.validate_supplier_id()
        if supplier_id is None:
            return
        supplier_name = self.validate_supplier_name()
        if supplier_name is None:
            return
        contact_info = self.validate_contact_info()
        if contact_info is None:
            return

        book_details = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "genre": genre,
            "total_copies": total_copies,
            "supplier": supplier_name
        }

        if self.confirm_details(book_details, "Book Details"):
            self.db["books"][i] = {
                "basic":
                {
                    "title": title,
                    "author": author,
                    "isbn": isbn,
                    "publication_year": publication_year,
                    "genre": genre,
                    "copies_available": copies_available
                },
                "category": {
                    "main_category": main_category,
                    "sub_category": sub_category
                },
                "location": {
                    "shelf": shelf,
                    "row": row,
                    "section": section
            },
              "reservation_queue":[],

                "inventory": {
                    "total_copies": total_copies,
                    "available_copies": available_copies,
                    "reserved_copies": reserved_copies,
                    "damaged_copies": damaged_copies,
                    "lost_copies": lost_copies
            },
                "restrictions": {
                    "age_restriction": age_restriction,
                    "membership_restriction": membership_restriction,
                    "borrowing_limit": borrowing_limit
            },
                "supplier": {

                    "supplier_id": supplier_id,
                    "supplier_name": supplier_name,
                    "contact_info": contact_info
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

            # COPIES AVAILABLE
            copies_available = input(
                f"Copies Available ({book['basic']['copies_available']}): "
            )
            if self.is_return_input(copies_available):
                return
            if copies_available:
                new_copies_available = self.validate_number(
                    "copies available"
                )
                if new_copies_available is None:
                    return
                book["basic"]["copies_available"] = new_copies_available

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
                new_membership_restriction = self.validate_text("membership restriction")
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
