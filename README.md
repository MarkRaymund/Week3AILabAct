# -*- coding: utf-8 -*-
"""Week3- Lab Activity 1.ipynb


**Activity 1: Aliah's Interactive Library Kiosk**

Aliah has moved on to her next project: an interactive kiosk for the school library that asks students questions directly and decides what they can borrow, based on their answers. Unlike the cafeteria assistant, this one needs to actually talk to the user through `input(`) in real time.

Rules:

*   A student can borrow a book if they have no overdue books AND their borrower status is "active".

*   If a student has overdue books, they must return them first — no new borrowing allowed, regardless of status.

*   If a student's status is "suspended", they cannot borrow anything, even with no overdue books.

*   Students with an active status and no overdue books can borrow up to 3 books at a time. If they try to borrow more than 3, the kiosk should warn them and only allow 3.

*   The kiosk should keep asking for the next student until someone types "exit" as their name.


**Your task:**


1.   Write a function `check_borrowing(overdue_books, status)` that returns `"Borrowing allowed"`, `"Not allowed: overdue books"`, or `"Not allowed: suspended account"` based on the rules.

2.   Using `input()`, ask the student for their **name**, whether they have **overdue books** (yes/no), their **status** (active/suspended), and **how many books they want to borrow**.

3.   Use the result of `check_borrowing()` to decide what message to show. If borrowing is allowed, also check the number of books requested and cap it at 3 with a warning message if needed.

4.   Wrap everything in a `while True` loop so the kiosk can process multiple students, and make it stop when someone types "exit" as their name.

5.   Keep a running counter of how many students were `successfully allowed to borrow books`, and print the total when the kiosk session ends.

6.   What happens if a student types "Yes" instead of "yes" for overdue books, or "Active" instead of "active" for status? How should Aliah's code handle these input variations so the kiosk doesn't break? (Hint: think back to `.lower()` from the assistant activity.)

7.   The rules say overdue books block borrowing **"regardless of status"** — meaning even an active-status student with overdue books is blocked. Why did Aliah write the overdue check as a priority condition, and what would go wrong if she checked status first instead?

8.   What if a student has no overdue books, active status, but tries to borrow 0 books? Should the kiosk treat this as valid input or an error? Modify your code to handle this edge case gracefully.



**Activity 2: Aliah's Cafeteria Queue Assistant**

Aliah has been asked by the school cafeteria staff to build a simple rule-based Python program that manages a fast lane during lunch break.

Students can use the fast lane only if they meet certain conditions, and Aliah needs help coding the logic.

Rules:

*   A student qualifies for the fast lane if they have less than 10 minutes
remaining in their break AND are buying 3 items or fewer.

*   If a student has a teacher's pass, they always qualify for the fast lane, regardless of time or item count.

*   If a student doesn't qualify, the program should tell them how many minutes they have left and suggest they use the regular line.

The cafeteria also wants to track how many students used the fast lane today.


Sample data to test with:

```
students_in_line = [
    {"name": "Marco", "minutes_left": 8, "items": 2, "teacher_pass": False},
    {"name": "Diane", "minutes_left": 15, "items": 1, "teacher_pass": False},
    {"name": "Kyle", "minutes_left": 5, "items": 6, "teacher_pass": False},
    {"name": "Ella", "minutes_left": 20, "items": 5, "teacher_pass": True},
]
```
Your task:

1.   Write a function check_fast_lane(minutes_left, items, teacher_pass) that returns "Fast lane approved" or "Use regular line" based on the rules above.

2.   Loop through students_in_line and print each student's name with their result.

3.   Add a counter that tallies how many students were approved for the fast lane, and print the total at the end.

4.   Ella has 20 minutes left and 5 items — normally she wouldn't qualify — but she has a teacher's pass.

5.   Explain in 5-9 sentences why rule-based systems need explicit "override" conditions like this, and what might go wrong if Aliah forgets to code the override check before the time/item check instead of after.

What if two rules conflict — EXAMPLE a student has a teacher's pass but the cafeteria is currently closed for cleaning?

How would Aliah's program need to change to handle a rule that overrides even the teacher's pass
"""