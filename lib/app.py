from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import Session, declarative_base, validates
from models.models import *
from collections import Counter
from termcolor import colored, cprint
import inquirer

engine = create_engine('sqlite:///bookshelf.db')
Base.metadata.create_all(engine)

def main():
    with Session(engine) as session:
        #PRIMARY STARTER MENU
        def main_menu():
            questions = [
                inquirer.List(
                    "starter_menu",
                    message = "Welcome to GooderReads! Which bookshelf would you like to view?",
                    choices = [
                        "View all of my books.",
                        "View or edit my want to read books.",
                        "View my currently reading books.",
                        "View my completed books.",
                        "Exit."
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["starter_menu"] ==   "View all of my books.":
                view_all()
            elif response["starter_menu"] == "View or edit my want to read books.":
                wtr_main()
            elif response["starter_menu"] == "View my currently reading books.":
                cr_main()
            elif response["starter_menu"] == "View my completed books.":
                completed_main()
            else:
                exit()


        #View a list of all the books on your bookshelf. 
        def view_all():
            print(f"Here's a list of all the books on your bookshelf: \n{session.query(Book).all()}")
            main_menu()


#################################################### WANT TO READ ####################################################
        def wtr_main():
            questions = [
                inquirer.List(
                    "wtr_main_menu",
                    message = "What do you want to do with your Want To Read Books?",
                    choices = [
                        "View all my want to read books.",
                        "Add a book to my want to read list.",
                        "Edit a book currently in my want to read list", 
                        "See a list of all the authors on my want to read list.",
                        "<-- Go Back."
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["wtr_main_menu"] == "View all my want to read books.":
                view_wtr()
            elif response["wtr_main_menu"] == "Add a book to my want to read list.":
                add_wtr()
            elif response["wtr_main_menu"] == "Edit a book currently in my want to read list":
                edit_wtr_menu()
            elif response["wtr_main_menu"] == "See a list of all the authors on my want to read list.":
                wtr_authors()
            else:
                main_menu()

        #set a method to return to wtr main or to program main menu
        def wtr_return_prompt():
            questions = [
                inquirer.List(
                "wtr_return",
                message = "Do you want to return to the Want to Read selection screen, or back to the main menu?",
                choices = [
                    "Return to Want to Read",
                    "Return to Main Menu"
                ]
            )
        ]
            response = inquirer.prompt(questions)
            if response["wtr_return"] == "Return to Want to Read":
                wtr_main()
            else:
                main_menu()

        #view all the books on wtr list
        def view_wtr():
            all_wtr = session.query(Book).filter(Book.bookshelf_id == 2).all()
            print(all_wtr)

            wtr_return_prompt()

        #add a new book to the wtr list
        def add_wtr():
            new_title = input("What's the title of the book you want to read?: ")
            new_author = input(f"Who is the author of {new_title}?: ")
            new_description = input(f"OPTIONAL: Write a description for the book, {new_title}: ")
            new_page_count = input(f"How many pages are in the book {new_title}?: ")

            new_wtr = Book(
                title = new_title,
                author = new_author,
                description = new_description,
                page_count = int(new_page_count),
                pages_read = 0,
                type = "Want To Read",
                star_rating = None,
                personal_review = None,
                bookshelf_id = 2
            )

            session.add(new_wtr)
            session.commit()

            cprint(f"\nGreat, I've added the book, {new_title}, to your Want to Read list!\n", "red")

            wtr_return_prompt()

        #edit the details of a book on your wtr list - edit, delete, or move
        def edit_wtr_menu():
            questions = [
                inquirer.List(
                    "edit_wtr_menu",
                    message = "What do you want to do?",
                    choices = [
                        "Edit the details for a book that's currently on my Want to Read list",
                        "Delete a book from my Want to Read list",
                        "Move a book from my Want to Read List to my Currently Reading list.", 
                        "<-- Go Back"
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["edit_wtr_menu"] == "Edit the details for a book that's currently on my Want to Read list":
                edit_wtr_details_menu()
                pass
            elif response["edit_wtr_menu"] == "Delete a book from my Want to Read list":
                del_wtr()
                pass
            elif response["edit_wtr_menu"] == "Move a book from my Want to Read List to my Currently Reading list.":
                move_wtr()
                pass
            else:
                wtr_main()

        #edit a book on your Want to Read list
        def edit_wtr_details_menu():
            print(f"Here are the books that are on your Want To Read list: {session.query(Book).filter(Book.bookshelf_id == 2).all()}")
            title_to_edit = input("Please type in the title of the book that you would like to edit: ")
            questions = [
                inquirer.List(
                    "confirm_edit_wtr",
                    message = f"Confirming... do you really want to edit the book, {title_to_edit}, on your Want to Read list?",
                    choices = [
                         f"Yes, edit {title_to_edit}",
                         f"No. Take me back home.",
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["confirm_edit_wtr"] == f"Yes, edit {title_to_edit}":
                book_edit = session.query(Book).filter(Book.title == title_to_edit).first()
                new_title = input("Confirm or edit the title of this book: ")
                new_author = input("Confirm or edit the authors name: ")
                new_description = input("Confirm or edit the book description: ")
                new_page_count = input("Confirm or edit the books page count: ")

                book_edit.title = new_title
                book_edit.author = new_author
                book_edit.description = new_description
                book_edit.page_count = new_page_count

                session.add(book_edit)
                session.commit()
                cprint(f"\nAwesome, that book has been updated! Here are the new details: \n {book_edit}", "red") 
                wtr_return_prompt()
            else:
                wtr_main()

        #delete a book from want to read 
        def del_wtr():
            print(f"Here are the books that are on your Want To Read list: {session.query(Book).filter(Book.bookshelf_id == 2).all()}")
            title_to_delete = input("Please type in the title of the book that you would like to delete: ")
            questions = [
                    inquirer.List(
                        "confirm_del",
                        message = f"Confirming... Do you really want to permanently delete the book, {title_to_delete}, from your Want to Read List?",
                        choices = [
                            f"Yes, delete {title_to_delete}",
                            f"No. Take me back home.",
                        ]
                    )
                ]
            response = inquirer.prompt(questions)
            if response["confirm_del"] == f"Yes, delete {title_to_delete}":
                book_del = session.query(Book).filter(Book.title == title_to_delete).first()
                session.delete(book_del)
                session.commit()
                cprint("\nOkay, that book has now been permanently deleted from your Want to Read list.\n", "red")
                wtr_return_prompt()
            else:
                wtr_main()

        #see all the authors that are on your want to read list
        def wtr_authors():
            all_wtr = session.query(Book).filter(Book.bookshelf_id == 2).all()
            all_authors = []
            i = 0
            while i < len(all_wtr):
                all_authors.append(all_wtr[i].author)
                i += 1
            cprint(f"\nHere's a list of all the authors on your Want to Read list: {list(set(all_authors))}\n", "red")
            wtr_return_prompt()

        #move a want to read book to currently reading list
        def move_wtr():
            print(f"Books on your Want to Read list: {session.query(Book).filter(Book.bookshelf_id == 2).all()}")
            title_to_move = input("Please type in the title of the book that you would like to move to Currently Reading: ")
            questions = [
                    inquirer.List(
                        "confirm_move",
                        message = f"Confirming... Do you really want to move {title_to_move} to your Currently Reading list?",
                        choices = [
                            f"Yes, move {title_to_move} to Currently Reading",
                            f"No. Take me back home.",
                        ]
                    )
                ]
            response = inquirer.prompt(questions)
            if response["confirm_move"] == f"Yes, move {title_to_move} to Currently Reading":
                book_move = session.query(Book).filter(Book.title == title_to_move).first()
                book_move.type = "Currently Reading"
                book_move.bookshelf_id = 1
                page_q = input("Working on moving... Please enter what page you're currently on for this book (if 0, enter 0): ")
                book_move.pages_read = int(page_q)
                session.add(book_move)
                session.commit()
                cprint(f"\nThanks! {title_to_move} has been moved from your Want to Read list to your Currently Reading list.\n", "red")
                cprint(book_move, "red")
                wtr_return_prompt()
            else:
                wtr_main()

#################################################### CURRENTLY READING ####################################################
        def cr_main():
            questions = [
                inquirer.List(
                    "cr_main_menu",
                    message = "What do you want to do with your currently reading books?",
                    choices = [
                        "View all my currently reading books.",
                        "Update the progress on a book you're currently reading.",
                        "Edit the details for a book you're currently reading",
                        "Move a book from currently reading to completed.",
                        "<-- Go Back."
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["cr_main_menu"] == "View all my currently reading books.":
                view_cr()
            elif response["cr_main_menu"] == "Update the progress on a book you're currently reading.":
                update_cr()
                pass
            elif response["cr_main_menu"] == "Edit the details for a book you're currently reading":
                edit_cr()
                pass
            elif response["cr_main_menu"] == "Move a book from currently reading to completed.":
                move_cr()
                pass
            else:
                main_menu()

        #set a method to return to cr main or to program main menu
        def cr_return_prompt():
            questions = [
                inquirer.List(
                "cr_return",
                message = "Do you want to return to the Currently Reading selection screen, or back to the main menu?",
                choices = [
                    "Return to Currently Reading",
                    "Return to Main Menu"
                ]
            )
        ]
            response = inquirer.prompt(questions)
            if response["cr_return"] == "Return to Currently Reading":
                cr_main()
            else:
                main_menu()

        #view all books on your currently reading list
        def view_cr():
            print("Here's a list of all the books you're currently reading:")
            all_cr = session.query(Book).filter(Book.bookshelf_id == 1).all()
            print(all_cr)

            cr_return_prompt()

        #update the page progress on a book that's in currently reading
        def update_cr():
            print(f"Here's a list of all the books you're currently reading: {session.query(Book).filter(Book.bookshelf_id == 1).all()}")
            title_to_update = input("Please type the name of the book that you want to update the current page for: ")
            book_edit = session.query(Book).filter(Book.title == title_to_update).first()
            book_edit.pages_read = input("What page of the book are you on now?: ")

            #check to see if the user has read all the pages in the book. If so, confirm and move to completed books.
            if book_edit.pages_read == book_edit.page_count or book_edit.pages_read > book_edit.page_count:
                questions = [
                    inquirer.List(
                        "move_to_complete",
                        message = f"Nice! Based on the page number you entered, it looks like you've finished the book, {title_to_update}! Do you want to move it to your Completed Books list?",
                        choices = [
                            f"Yes! I've finished {title_to_update} and I want to mark it as COMPLETE.",
                            "No, I've mistyped. Take me back to the main Currently Reading selection."
                        ]
                    )
                ]
                response = inquirer.prompt(questions)
                if response["move_to_complete"] == f"Yes! I've finished {title_to_update} and I want to mark it as COMPLETE.":
                    new_star_rating = input("Sweet! Now that you've finished, please rate the book betwee 0 - 5 stars: ")
                    new_personal_review = input("If desired, please also leave a written personal review of the book: ")
                    book_edit.type = "Completed"
                    book_edit.bookshelf_id = 3
                    book_edit.pages_read = book_edit.page_count
                    book_edit.star_rating = int(new_star_rating)
                    book_edit.personal_review = new_personal_review
                    session.add(book_edit)
                    session.commit()
                    cprint(f"\nIt's lit! Congrats on finishing the book, {book_edit.title}! It's been moved from Currently Reading to Completed List.\n", "red")
                    cr_return_prompt()
                else:
                    cr_main()
            else:
                session.add(book_edit)
                session.commit()
                percent_complete = int(((book_edit.pages_read) / (book_edit.page_count))*100)
                def progress_bar():
                    if percent_complete == 0:
                        cprint ('|                        | 0% Complete', "green") 
                    elif 0 < percent_complete <= 4:
                        cprint (f'|█                       | {percent_complete}% Complete', "green")
                    elif 4 < percent_complete <= 8:
                        cprint (f'|██                      | {percent_complete}% Complete', "green")
                    elif 8 < percent_complete <= 12:
                        cprint (f'|███                     | {percent_complete}% Complete', "green")
                    elif 12 < percent_complete <= 16:
                        cprint (f'|████                    | {percent_complete}% Complete', "green")
                    elif 16 < percent_complete <= 20:
                        cprint (f'|█████                   | {percent_complete}% Complete', "green")
                    elif 20 < percent_complete <= 24:
                        cprint (f'|██████                  | {percent_complete}% Complete', "green")
                    elif 24 < percent_complete <= 28:
                        cprint (f'|███████                 | {percent_complete}% Complete', "green")
                    elif 28 < percent_complete <= 32:
                        cprint (f'|████████                | {percent_complete}% Complete', "green")
                    elif 32 < percent_complete <= 36:
                        cprint (f'|█████████               | {percent_complete}% Complete', "green")
                    elif 36 < percent_complete <= 40:
                        cprint (f'|██████████              | {percent_complete}% Complete', "green")
                    elif 40 < percent_complete <= 44:
                        cprint (f'|██████████              | {percent_complete}% Complete', "green")
                    elif 44 < percent_complete <= 48:
                        cprint (f'|███████████             | {percent_complete}% Complete', "green")
                    elif 48 < percent_complete <= 52:
                        cprint (f'|████████████            | {percent_complete}% Complete', "green")
                    elif 52 < percent_complete <= 56:
                        cprint (f'|█████████████           | {percent_complete}% Complete', "green")
                    elif 56 < percent_complete <= 60:
                        cprint (f'|██████████████          | {percent_complete}% Complete', "green")
                    elif 60 < percent_complete <= 64:
                        cprint (f'|███████████████         | {percent_complete}% Complete', "green")
                    elif 64 < percent_complete <= 68:
                        cprint (f'|████████████████        | {percent_complete}% Complete', "green")
                    elif 68 < percent_complete <= 72:
                        cprint (f'|█████████████████       | {percent_complete}% Complete', "green")
                    elif 72 < percent_complete <= 76:
                        cprint (f'|██████████████████      | {percent_complete}% Complete', "green")
                    elif 76 < percent_complete <= 80:
                        cprint (f'|███████████████████     | {percent_complete}% Complete', "green")
                    elif 80 < percent_complete <= 84:
                        cprint (f'|████████████████████    | {percent_complete}% Complete', "green")
                    elif 84 < percent_complete <= 88:
                        cprint (f'|█████████████████████   | {percent_complete}% Complete', "green")
                    elif 88 < percent_complete <= 92:
                        cprint (f'|██████████████████████  | {percent_complete}% Complete', "green")
                    elif 92 < percent_complete <= 96:
                        cprint (f'|██████████████████████  | {percent_complete}% Complete', "green")
                    elif 96 < percent_complete <= 99:
                        cprint (f'|███████████████████████ | {percent_complete}% Complete', "green")
                    elif percent_complete == 100:
                        cprint (f'|█████████████████████████| {percent_complete}% Complete', "green")
                      
                cprint(f"\nI've updated your progress on that book. Here's all the details of that book: \n {book_edit}", "red")
                cprint(f"\nYou're now {percent_complete}% done with {book_edit.title}.\n", "green")
                progress_bar()
                print("\n")
                cr_return_prompt()
            
        #edit the details of a book you're currently reading:
        def edit_cr():
            print(f"Here are the books you're currently reading: {session.query(Book).filter(Book.bookshelf_id == 1).all()}")
            title_to_edit = input("Please type in the title of the book that you would like to edit: ")
            questions = [
                    inquirer.List(
                        "confirm_edit",
                        message = f"Confirming... Do you really want to edit the book, {title_to_edit}, from your Currently Reading List?",
                        choices = [
                            f"Yes, edit {title_to_edit}",
                            f"No. Take me back home.",
                        ]
                    )
                ]
            response = inquirer.prompt(questions)
            if response["confirm_edit"] == f"Yes, edit {title_to_edit}":
                book_edit = session.query(Book).filter(Book.title == title_to_edit).first()
                new_title = input("Confirm or edit the title of this book: ")
                new_author = input("Confirm or edit the authors name: ")
                new_description = input("Confirm or edit the book description: ")
                new_page_count = input("Confirm or edit the books page count: ")
                new_pages_read = input("Confirm or edit the current page that you're on: ")

                book_edit.title = new_title
                book_edit.author = new_author
                book_edit.description = new_description
                book_edit.page_count = new_page_count
                book_edit.pages_read = new_pages_read

                session.add(book_edit)
                session.commit()
                cprint(f"\nAwesome, that book has been updated! Here are the new details: \n {book_edit}", "red")
                cr_return_prompt()
            else: 
                cr_main()

        #move a book from currently reading to your completed books list
        def move_cr():
            print(f"Here are the books on your Currently Reading list: {session.query(Book).filter(Book.bookshelf_id == 1).all()}")
            impt_text= colored("IMPORTANT:", "red")
            title_to_move = input(f"Please type in the title of the book that you would like to move to your Completed Books list.\n{impt_text} This action will automatically update the number of pages you've read to match the total pages in this book: ")
            questions = [
                inquirer.List(
                    "confirm_move",
                    message = f"Confirming... Do you really want to mark the book, {title_to_move}, as COMPLETE?",
                    choices = [
                        f"Yes, I want to mark {title_to_move} as COMPLETE.",
                        f"No. Take me back home."
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["confirm_move"] == f"Yes, I want to mark {title_to_move} as COMPLETE.":
                book_move = session.query(Book).filter(Book.title == title_to_move).first()
                new_star_rating = input("Sweet! Now that you've finished, please rate the book betwee 0 - 5 stars: ")
                new_personal_review = input("If desired, please also leave a written personal review of the book: ")
                book_move.type = "Completed"
                book_move.bookshelf_id = 3
                book_move.pages_read = book_move.page_count
                book_move.star_rating = int(new_star_rating)
                book_move.personal_review = new_personal_review
                session.add(book_move)
                session.commit()
                cprint(f"\nIt's lit! Congrats on finishing the book, {book_move.title}! It's been moved from Currently Reading to Completed List.\n", "red")
                cprint(f"{book_move}", "red")
                cr_return_prompt()
            else:
                main_menu()



#################################################### COMPLETED BOOKZ ####################################################
        def completed_main():
            questions = [
                inquirer.List(
                    "completed_main_menu",
                    message = "What do you want to do with your completed books?",
                    choices = [
                        "View all my completed books.",
                        "Get cool stats on the books I've finished.",
                        "Edit a book on your completed list",
                        "Remove a book from your completed list.",
                        "<-- Go Back."
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["completed_main_menu"] == "View all my completed books.":
                view_cb()
                pass
            elif response["completed_main_menu"] == "Get cool stats on the books I've finished.":
                cool_cb_stats()
                pass
            elif response["completed_main_menu"] == "Edit a book on your completed list":
                edit_cb()
                pass
            elif response["completed_main_menu"] == "Remove a book from your completed list.":
                remove_cb()
                pass
            else:
                main_menu()

        #create a method to return back to completed_main() or main_menu() 
        def cb_return_prompt():
            questions = [
                inquirer.List(
                "cb_return",
                message = "Do you want to return to the Completed Books selection screen, or back to the main menu?",
                choices = [
                    "Return to Completed Books",
                    "Return to Main Menu"
                ]
            )
        ]
            response = inquirer.prompt(questions)
            if response["cb_return"] == "Return to Completed Books":
                completed_main()
            else:
                main_menu()
        
        #view all completed books
        def view_cb():
            cprint("\nHere's a list of all the books you've finished reading: \n", "red")
            all_cb = session.query(Book).filter(Book.bookshelf_id == 3).all()
            cprint(all_cb, "red")

            cb_return_prompt()

        #get sick stats regarding your completed books
        def cool_cb_stats():
            questions = [
                inquirer.List(
                    "cool_stats",
                    message = "Alright, what do you want to know?",
                    choices = [
                        "How many books have I completed in total?",
                        "How many total pages have I read across all completed books?",
                        "Who is the author I've read the most of across all completed books?",
                        "<-- Go Back"
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["cool_stats"] == "How many books have I completed in total?":
                total_completed_books()
            elif response["cool_stats"] == "How many total pages have I read across all completed books?":
                calc_total_pages()
                pass
            elif response["cool_stats"] == "Who is the author I've read the most of across all completed books?":
                calc_top_author()
                pass
            else:
                completed_main()
        
        #Get the number of total books you've completed
        def total_completed_books():
            all_cb = session.query(Book).filter(Book.bookshelf_id == 3).all()
            cprint(f"\nAltogether, you've read and finished {len(all_cb)} books!\n", "red")
            cb_return_prompt()

        #calculate the total number of pages someone has read across all their completed books
            #more effecient example: https://www.phind.com/search?cache=myqxiy1stelsxf3v9i4t6e72 
        def calc_total_pages():
            all_cb = session.query(Book).filter(Book.bookshelf_id == 3).all()
            total_pages = 0;
            i = 0
            while i < len(all_cb):
                total_pages += all_cb[i].page_count
                i += 1
            cprint(f"\nIn total, you have read {total_pages} pages!\n", "red")
            cb_return_prompt()

        #calculate the author that has been read the most 
        def calc_top_author():
            all_cb = session.query(Book).filter(Book.bookshelf_id == 3).all()
            all_authors = []
            i = 0
            while i < len(all_cb):
                all_authors.append(all_cb[i].author)
                i+=1
            author_counts = Counter(all_authors)
            top_author = author_counts.most_common(1)
            cprint(f"\nYour top author in your Completed Books list is: {(top_author[0][0]).upper()}\n", "red")  
            cb_return_prompt()

        #edit a book you've completed
        def edit_cb():
            print(f"Here are the books on your Completed Books list: {session.query(Book).filter(Book.bookshelf_id == 3).all()}")
            title_to_edit = input("Please type in the title of the book that you would like to edit: ")
            questions = [
                    inquirer.List(
                        "confirm_edit",
                        message = f"Confirming... Do you really want to edit the book, {title_to_edit}, from your Completed Book List?",
                        choices = [
                            f"Yes, edit {title_to_edit}",
                            f"No. Take me back home.",
                        ]
                    )
                ]
            response = inquirer.prompt(questions)
            if response["confirm_edit"] == f"Yes, edit {title_to_edit}":
                book_edit = session.query(Book).filter(Book.title == title_to_edit).first()
                new_title = input("Confirm or edit the title of this book: ")
                new_author = input("Confirm or edit the authors name: ")
                new_description = input("Confirm or edit the book description: ")
                new_page_count = input("Confirm or edit the books page count: ")
                new_star_rating = input("Confirm or edit the star rating (0 - 5) for this book: ")
                new_personal_review = input("Confirm or edit your personal review for this book: ")

                book_edit.title = new_title
                book_edit.author = new_author
                book_edit.description = new_description
                book_edit.page_count = new_page_count
                book_edit.pages_read = new_page_count
                book_edit.star_rating = int(new_star_rating)
                book_edit.personal_review = new_personal_review

                session.add(book_edit)
                session.commit()

                cprint(f"\nAwesome, that book has been updated! Here are the new details: \n {book_edit}\n", "red")

                cb_return_prompt()
            else:
                completed_main()

        #remove a book from your completed books list
        def remove_cb():
            print(f"Here's a list of your current completed books: {session.query(Book).filter(Book.bookshelf_id == 3).all()}")
            title_to_delete = input("Please type in the title of the book you want to delete: ")
            questions = [
                inquirer.List(
                    "confirm_del",
                    message = f"Confirming... do you really want to permanently delete the book, {title_to_delete}, from your Completed Books list?",
                    choices = [
                        f"Yes, delete {title_to_delete}",
                        f"No. Take me back home."
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["confirm_del"] == f"Yes, delete {title_to_delete}":
                book_del = session.query(Book).filter(Book.title == title_to_delete).first()
                session.delete(book_del)
                session.commit()
                cprint("\nOkay, that book has now been permanently deleted from your Completed Books list.\n", "red")
                cb_return_prompt()
            else:
                completed_main()
            
        cprint('''
                                                                                                                                                         
                                                                                                                                                  
  ,----..                                                                   ,-.----.                                                              
 /   /   \                               ,---,                              \    /  \                                  ,---,                      
|   :     :     ,---.      ,---.       ,---.'|              __  ,-.         ;   :    \                               ,---.'|                      
.   |  ;. /    '   ,'\    '   ,'\      |   | :            ,' ,'/ /|         |   | .\ :                               |   | :   .--.--.            
.   ; /--`    /   /   |  /   /   |     |   | |    ,---.   '  | |' |         .   : |: |     ,---.      ,--.--.        |   | |  /  /    '           
;   | ;  __  .   ; ,. : .   ; ,. :   ,--.__| |   /     \  |  |   ,'         |   |  \ :    /     \    /       \     ,--.__| | |  :  /`./           
|   : |.' .' '   | |: : '   | |: :  /   ,'   |  /    /  | '  :  /           |   : .  /   /    /  |  .--.  .-. |   /   ,'   | |  :  ;_             
.   | '_.' : '   | .; : '   | .; : .   '  /  | .    ' / | |  | '            ;   | |  \  .    ' / |   \__\/: . .  .   '  /  |  \  \    `.          
'   ; : \  | |   :    | |   :    | '   ; |:  | '   ;   /| ;  : |            |   | ;\  \ '   ;   /|   ," .--.; |  '   ; |:  |   `----.   \         
'   | '/  .'  \   \  /   \   \  /  |   | '/  ' '   |  / | |  , ;            :   ' | \.' '   |  / |  /  /  ,.  |  |   | '/  '  /  /`--'  /         
|   :    /     `----'     `----'   |   :    :| |   :    |  ---'             :   : :-'   |   :    | ;  :   .'   \ |   :    :| '--'.     /          
 \   \ .'                           \   \  /    \   \  /                    |   |.'      \   \  /  |  ,     .-./  \   \  /     `--'---'           
  `---`                              `----'      `----'                     `---'         `----'    `--`---'       `----'                       

              It's like goodreads, but gooder!!
      ''', "magenta")
    main_menu()

if __name__ == "__main__":
    main()
