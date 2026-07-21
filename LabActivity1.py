def check_borrowing(overdue_books, status):
    if overdue_books:
        return "Not allowed: overdue books"
 
    if status == "suspended":
        return "Not allowed: suspended account"
 
    return "Borrowing allowed"
 

def main():
    successful_borrowers = 0
 
    while True:
        name = input("\nEnter student name (or type 'exit' to close the kiosk): ").strip()
 
        if name.lower() == "exit":
            break
 
        overdue_input = input("Do you have overdue books? (yes/no): ").strip().lower()
        overdue_books = overdue_input == "yes"
 
        status = input("What is your borrower status? (active/suspended): ").strip().lower()
 
        books_input = input("How many books would you like to borrow? ").strip()
        try:
            num_books = int(books_input)
        except ValueError:
            print("That's not a valid number. Please start over for this student.")
            continue
 
        result = check_borrowing(overdue_books, status)
 
        if result == "Borrowing allowed":
            if num_books <= 0:
                print("You need to request at least 1 book to borrow. No books processed.")
            elif num_books > 3:
                print(f"You requested {num_books}, but the limit is 3 books at a time.")
                print("Warning: only 3 books will be issued.")
                successful_borrowers += 1
            else:
                print(f"Borrowing allowed. You may take {num_books} book(s). Enjoy!")
                successful_borrowers += 1
        else:
            print(result)
 
    print(f"\nKiosk session ended. Students who successfully borrowed books: {successful_borrowers}")
 
 
if __name__ == "__main__":
    main()
 