from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import Session, declarative_base, validates
from models import *
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
            ##note -- need to add a return prompt here


######################## WANT TO READ ########################
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
                #edit_wtr_menu()
                pass
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
                page_count = new_page_count,
                pages_read = 0,
                type = "Want To Read",
                star_rating = None,
                personal_review = None,
                bookshelf_id = 2
            )

            session.add(new_wtr)
            session.commit()

            print(f"Great, I've added the book, {new_title}, to your Want to Read list!")

            wtr_return_prompt()

        #NEEDS FINALIZING: edit the details of a book on your wtr list - select a book
        def edit_wtr_menu():
            all_wtr = session.query(Book).filter(Book.bookshelf_id == 2).all()
            indiv_book = []
            for book in all_wtr:
                book.push(indiv_book)

            questions = [
                inquirer.List(
                    "select_wtr_edit",
                    message = "Which book would you like to edit?"
                )
            ]

        def wtr_authors():
            all_wtr = session.query(Book).filter(Book.bookshelf_id == 2).all()
            all_authors = []
            i = 0
            while i < len(all_wtr):
                all_authors.append(all_wtr[i].author)
                i += 1
            print(set(all_authors))
            wtr_return_prompt()






######################## CURRENTLY READING ########################
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
                #update_cr_menu()
                pass
            elif response["cr_main_menu"] == "Edit the details for a book you're currently reading":
                #edit_cr()
                pass
            elif response["cr_main_menu"] == "Move a book from currently reading to completed.":
                #move_cr()
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

        def view_cr():
            print("Here's a list of all the books you're currently reading:")
            all_cr = session.query(Book).filter(Book.bookshelf_id == 1).all()
            print(all_cr)

            cr_return_prompt()

        #NEEDS FIXING: update the current page number of a book you're reading.
        def update_cr_menu():
            all_cr = session.query(Book).filter(Book.bookshelf_id == 1).all()
            if len(all_cr) == 1:
                print("You only have one book that you're currently reading. Let's update the current page of that book.")

                #See if there's only one book in CR - if so, immediately go into edit mode.
                pass
            else:
                #If there's more than one book, ask user which book they want to update the progress of.
                questions = [
                    inquirer.List(
                    "cr_update_select",
                    message = "Which book do you want to update the progress for?",
                    choices = [
                        ""
                    ]
                )
        ]


######################## COMPLETED BOOKZZZ ########################
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
                #view_cb()
                pass
            elif response["completed_main_menu"] == "Get cool stats on the books I've finished.":
                #cool_cb_stats()
                pass
            elif response["completed_main_menu"] == "Edit a book on your completed list":
                #edit_cb()
                pass
            elif response["completed_main_menu"] == "Remove a book from your completed list.":
                #remove_cb
                pass
            else:
                main_menu()
 
        print('''

+++ !!!Welcome to GooderReads!!! +++

      ''')
    main_menu()

if __name__ == "__main__":
    main()
