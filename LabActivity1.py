def check_borrowing(overdue_books,status):
    if overdue_books > 0:
        status = "Overdue"
    else:
        status = "Good Standing"
    return status