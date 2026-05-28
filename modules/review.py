# review for book 
from modules.validation import Validation

class ReviewModule(Validation):
    def review_book(self):
        user_id = self.validate_user_id()
        if not user_id:
            return
        book_id = input("Enter Book ID: ")
        if book_id.lower() == "return":
            return
        if book_id not in self.db["books"]:
            print("Book Not Found")
            return
        review = self.validate_text("review")
        rating = self.validate_rating()
        
        
        if "reviews" not in self.db["books"][book_id]:
            self.db["books"][book_id]["reviews"] = []
        self.db["books"][book_id]["reviews"].append({
            "user_id": user_id,
            "review": review,
            "rating": rating
        })
        print(f"Review added for book {book_id} by user {user_id}.")
        
    def view_reviews(self):
        book_id = input("Enter Book ID to view reviews: ")
        if book_id.lower() == "return":
            return
        if book_id not in self.db["books"]:
            print("Book Not Found")
            return
        if "reviews" not in self.db["books"][book_id] or not self.db["books"][book_id]["reviews"]:
            print("No reviews found for this book.")
            return
        for review in self.db["books"][book_id]["reviews"]:
            print(f"User ID: {review['user_id']}, Rating: {review['rating']}, Review: {review['review']}")
            
    def search_reviews_by_user(self):
        user_id = input("Enter User ID to search reviews: ")
        if user_id.lower() == "return":
            return
        if user_id not in self.db["users"] or self.db["users"][user_id]["user_status"] != "active":
            print("User Not Found or Inactive")
            return
        
        for book_id, book_info in self.db["books"].items():
            if "reviews" in book_info:
                for review in book_info["reviews"]:
                    if review["user_id"] == user_id:
                        print(f"Book ID: {book_id}, Rating: {review['rating']}, Review: {review['review']}")
                        found_reviews = True
        else:
            print("No reviews found for this user.")