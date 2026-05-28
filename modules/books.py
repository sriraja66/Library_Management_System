from database.database import Library
from modules.validation import Validation

class Books_module(Validation):
    #add book 

    def add_book(self):
        i = f"B{len(self.db['books']) + 1}"
        self.db["books"][i] = {
            "basic":
            {
                "title": self.validate_text("title"),
                "author": self.validate_text("author"),
                "isbn": self.validate_isbn(),
                "publication_year": self.validate_publication_year(),
                "genre": self.validate_text("genre"),
                "copies_available": self.validate_number("copies available")
            },
            "category": {
                "main_category": self.validate_text("main category"),
                "sub_category": self.validate_text("sub category")
            },
            "loacation": {
                "shelf": self.validate_number("shelf number"),
                "row": self.validate_number("row number"),
                "section": self.validate_text("section")
        },
          "reservation_queue":[],
          
            "inventory": {
                "total_copies": self.validate_number("total copies"),
                "available_copies": self.validate_number("available copies"),
                "reserved_copies": self.validate_number("reserved copies"),
                "damaged_copies": self.validate_number("damaged copies"),
                "lost_copies": self.validate_number("lost copies")
        },
            "restrictions": {
                "age_restriction": self.validate_number("age restriction"),
                "membership_restriction": self.validate_text("membership restriction"),
                "borrowing_limit": self.validate_number("borrowing limit")
        },
            "supplier": {
                
                "supplier_id": self.validate_supplier_id(),
                "supplier_name": self.validate_supplier_name(),
                "contact_info": self.validate_contact_info()
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
        if book_id.strip().lower == "return":
            return
        if book_id in self.db["books"]:
            book = self.db["books"][book_id]
            print("Leave Blank To Keep Old Value\n")

            # TITLE
            title = input(f"Title ({book['basic']['title']}): ")
            if title.strip().lower() == "return":
                return
            if title:
                book["basic"]["title"] = self.validate_text("title")

            # AUTHOR
            author = input(f"Author ({book['basic']['author']}): ")
            if author.strip().lower() == "return":  
                return  
            if author:
                book["basic"]["author"] = self.validate_text("author")

            # ISBN
            isbn = input(f"ISBN ({book['basic']['isbn']}): ")
            if isbn.strip().lower() == "return":
                return
            if isbn:
                book["basic"]["isbn"] = self.validate_isbn()

            # PUBLICATION YEAR
            publication_year = input(
                f"Publication Year ({book['basic']['publication_year']}): "
            )
            if publication_year.strip().lower() == "return":
                return
            if publication_year:
                book["basic"]["publication_year"] = self.validate_publication_year()

            # GENRE
            genre = input(f"Genre ({book['basic']['genre']}): ")
            if self.check_availability(genre):
                return
            if genre:
                book["basic"]["genre"] = self.validate_text("genre")

            # COPIES AVAILABLE
            copies_available = input(
                f"Copies Available ({book['basic']['copies_available']}): "
            )
            if copies_available is None:
                return
            if copies_available:
                book["basic"]["copies_available"] = self.validate_number(
                    "copies available"
                )
            
            # age restriction
            age_restriction = input(
                f"Age Restriction ({book['restrictions']['age_restriction']}): "
            )
            if age_restriction is None:
                return
            if age_restriction:
                book["restrictions"]["age_restriction"] = self.validate_number("age restriction")
                
            # membership restriction
            membership_restriction = input(
                f"Membership Restriction ({book['restrictions']['membership_restriction']}): "
            )
            if membership_restriction is None:
                return
            if membership_restriction:
                book["restrictions"]["membership_restriction"] = self.validate_text("membership restriction")
                
            # borrowing limit
            borrowing_limit = input(
                f"Borrowing Limit ({book['restrictions']['borrowing_limit']}): "
            )
            if borrowing_limit is None:
                return
            if borrowing_limit:
                book["restrictions"]["borrowing_limit"] = self.validate_number("borrowing limit")
                
            # supplier name
            supplier_name = input(
                f"Supplier Name ({book['supplier']['supplier_name']}): "
            )
            if supplier_name is None:   
                return
            if supplier_name:
                book["supplier"]["supplier_name"] = self.validate_text("supplier name")
            
            # supplier contact info
            contact_info = input(
                f"Supplier Contact Info ({book['supplier']['contact_info']}): "
            )
            if contact_info is None:
                return
            if contact_info:
                book["supplier"]["contact_info"] = self.validate_phone("supplier contact number")
            print(f"Book {book_id} updated successfully.")
            
            # location
            shelf = input(
                f"Shelf Location ({book['supplier']['shelf']}): "
            )
            if shelf is None:
                return
            if shelf:
                book["supplier"]["shelf"] = self.validate_text("shelf location")
            # row    
            row = input(
                f"Row Location ({book['supplier']['row']}): "
            )
            if row is None:
                return
            if row:
                book["supplier"]["row"] = self.validate_text("row location")
                
            # section 
            section = input(
                f"Section Location ({book['supplier']['section']}): "
            )
            if section is None:
                return
            if section:
                book["supplier"]["section"] = self.validate_text("section location")

        else:
            print("Book not found.")

    # search book

    def search_book(self):
        i = input("Enter book ID to search: ")
        if i in self.db["books"]:
            print(f"Book ID: {i}")
            for key, value in self.db["books"][i].items():
                print(f"{key}: {value}")
        else:
            print("Book not found.")

    # delete book

    def delete_book(self):
        book_id = input("Enter book ID to delete: ")
        if book_id in self.db["books"]:
            del self.db["books"][book_id]
            print(f"Book {book_id} deleted successfully.")
        else:
            print("Book not found.")

    # check availability

    def check_availability(self):
        book_id = input("Enter book ID to check availability: ")
        if book_id in self.db["books"]:
            available_copies = self.db["books"][book_id]["inventory"]["available_copies"]
            print(f"Book {book_id} has {available_copies} copies available.")
        else:
            print("Book not found.")

   

