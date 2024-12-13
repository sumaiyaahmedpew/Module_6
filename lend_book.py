from datetime import datetime, timedelta
import json
import save_all_books

def lend_book(all_books):
    borrower_name = input("Enter Borrower's Name: ")
    borrower_phone = input("Enter Borrower's Phone Number: ")
    book_title = input("Enter Book Title to Lend: ")
    
    for book in all_books:
        if book["title"] == book_title:
            if book["quantity"] > 0:
                due_date = datetime.now() + timedelta(days=14)  # 2 weeks from now
                lend_info = {
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "book_title": book_title,
                    "due_date": due_date.strftime("%d-%m-%Y")
                }
                
                with open("lend_info.json", "r+") as fp:
                    try:
                        lend_data = json.load(fp)
                    except json.JSONDecodeError:
                        lend_data = []
                    lend_data.append(lend_info)
                    fp.seek(0)
                    json.dump(lend_data, fp, indent=4)
                
                book["quantity"] -= 1  # Reduce quantity
                save_all_books.save_all_books(all_books)
                
                print(f"Book '{book_title}' lent successfully! Due date: {due_date.strftime('%d-%m-%Y')}")
                return all_books
            else:
                print("There are not enough books available to lend.")
                return all_books
    
    print("Book not found.")
    return all_books
