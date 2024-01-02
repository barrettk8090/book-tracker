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
                pass
            elif response["starter_menu"] == "View my completed books.":
                pass
            else:
                exit()

        #View a list of all the books on your bookshelf. 
        def view_all():
            print(f"Here's a list of all the books on your bookshelf: \n{session.query(Book).all()}")
#### WANT TO READ ####
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


        
        print('''

+++ !!!Welcome to GooderReads!!! +++

      ''')
    main_menu()

if __name__ == "__main__":
    main()
