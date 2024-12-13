import json
import save_all_books

def return_book(all_books):
    borrower_name = input("Enter Borrower's Name: ")
    book_title = input("Enter Book Title to Return: ")
    
    with open("lend_info.json", "r+") as fp:
        try:
            lend_data = json.load(fp)
        except json.JSONDecodeError:
            lend_data = []
        
        for entry in lend_data:
            if entry["borrower_name"] == borrower_name and entry["book_title"] == book_title:
                lend_data.remove(entry)
                fp.seek(0)
                fp.truncate()
                json.dump(lend_data, fp, indent=4)
                
                for book in all_books:
                    if book["title"] == book_title:
                        book["quantity"] += 1  # Increase quantity
                        save_all_books.save_all_books(all_books)
                        print(f"Book '{book_title}' returned successfully!")
                        return all_books
        
        print("No matching lend record found.")
        return all_books
