class Library:

    def __init__(self):

        self.db = {
            "users": {},
            "books": {},
            "suppliers": {},
            "roles": {
                "admin": {
                    "permissions": ["all"]
                },
                "librarian": {
                    "permissions": [
                        "add_book",
                        "remove_book",
                        "search_books",
                        "fine_collection",
                        "inventory_management"
                    ]
                },
                "member": {
                    "permissions": [
                        "search",
                        "reserve",
                        "review"
                    ]
                }
            },
            "settings": {
                "library_name": "City Library",
                "fine_per_day": 20,
                "memberships": {
                    "basic": {
                        "book_limit": 5,
                        "reservation_limit": 2,
                        "fine_discount": 0,
                        "max_reservation_days": 7
                    },
                    "premium": {
                        "book_limit": 10,
                        "reservation_limit": 5,
                        "fine_discount": 0.5,
                        "max_reservation_days": 14
                    }
                }
            }
        }