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
                # view_all_wtr()
                pass
            elif response["wtr_main_menu"] == "Add a book to my want to read list.":
                # add_wtr()
                pass
            elif response["wtr_main_menu"] == "Edit a book currently in my want to read list":
                #edit_wtr_menu()
                pass
            elif response["wtr_main_menu"] == "See a list of all the authors on my want to read list.":
                #wtr_authors()
                pass
            else:
                main_menu()

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
                #view_cr()
                pass
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
