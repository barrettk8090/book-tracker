from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import Session, declarative_base, validates
from models import *
from seeds import *
import inquirer


#If this doesnt work be sure to comment back create engine at the bottom of models.oy

engine = create_engine('sqlite:///bookshelf.db')
Base.metadata.create_all(engine)

def main():
    with Session(engine) as session:
        #Main menu
        def main_menu():
            questions = [
                inquirer.List(
                    "starter_menu",
                    message = "Welcome to GooderReads! What would you like to do?",
                    choices = [
                        "View all the books on your Bookshelf",
                        "View or edit the books in your 'Want to Read' list",
                        "View or edit the books you're 'Currently Reading'",
                        "View all of your completed books",
                        "Exit"
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["starter_menu"] ==  "View all the books on your Bookshelf":
                view_bookshelf()
            elif response["starter_menu"] == "View or edit the books in your 'Want to Read' list":
                want_to_read_menu()
            elif response["starter_menu"] == "View or edit the books you're 'Currently Reading'":
                pass
            elif response["starter_menu"] == "View all of your completed books":
                pass
            else:
                exit()


## View all of the books on your bookshelf - ask David
        def view_bookshelf():
            print("Here's a list of all the books on your bookshelf:")

####### WANT TO READ ######
            
        def want_to_read_menu():
            questions = [
                inquirer.List(
                    "want_to_read_main",
                    message = "WANT TO READ: Make a selection.",
                    choices = [
                        "View all the books on your Want To Read list.",
                        "Edit a book on your Want To Read list.",
                        "Add a new book to your Want To Read list.",
                        "Move a book from Want To Read to your Currently Reading pile.",
                        "Move a book from Want to Read to your Completed Books pile.",
                        "<-- Go Back"
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["want_to_read_main"] == "View all the books on your Want To Read list.":
                all_wtr()
            elif response["want_to_read_main"] == "Edit a book on your Want To Read list.":
                #Which book do you want to edit the details of?
                pass
            elif response["want_to_read_main"] == "Add a new book to your Want To Read list.":
                #prompt user for the details of the book and add it to the WTR list
                add_wtr()
            elif response ["want_to_read_main"] == "Move a book from Want To Read to your Currently Reading pile.":
                #idk figure out how to do this - delete from WTR, prompt user for any missing details from current, add to Currently Reading
                pass
            elif response ["want_to_read_main"] == "Move a book from Want to Read to your Completed Books pile.":
                #same as above but prompt for details for completed books pile (star rating, review, etc)
                pass
            else:
                main_menu()

    #show all want to read books
        def all_wtr():
            all_books = session.query(WantToRead).all()
            print(f'Here\'s a list of all the books that are currently on your Want To Read list: {all_books}')
    #edit a want to read book -- INCOMPLETE
        def edit_wtr_initial():
            all_books = session.query(WantToRead).all()
                #loop through all books
                #for each book, pop it from the array and assign it to a unique variable - can we use the ID??
            for book in all_books:
                book.id
            questions = [
                inquirer.List(
                    "edit_wtr",
                    message = "Which book do you want to edit the details of?",
                )
            ]
    #add a new book to the want to read list
        def add_wtr():
            title1 = input("What is the title of the book you want to add?")
            author1 = input(f"Who is the author of {title1}?")
            description1 = input(f"Write a description for the book {title1}. If you don't have one, you can leave this field blank.")
            page_count1 = input(f"How many pages are in the book {title1}?")

            newb = add_want_to_read(session, title1, author1, description1, page_count1)
            session.add(newb)
            session.commit()


#### CURRENTLY READING #####
        def currently_reading_menu():
            questions = [
                inquirer.List(
                    "currently_reading_main",
                    message = "CURRENTLY READING: Make a selection",
                    choices = [
                        "View all the books you're currently reading",
                        "Edit or update a book on your Currently Reading List",
                        "Add a new book to your Currently Reading List.",
                        "Move a book from Currently Reading to your Completed pile",
                        "<-- Go Back"
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["currently_reading_main"] ==  "View all the books you're currently reading":
                pass
            elif response["currently_reading_main"] == "Edit or update a book on your Currently Reading List":
                pass
            elif response["currently_reading_main"] == "Add a new book to your Currently Reading List.":
                pass
            elif response["currently_reading_main"] == "Move a book from Currently Reading to your Completed pile":
                pass
            else:
                main_menu()

#### COMPLETED BOOKS ####
            def completed_books_menu():
                questions = [
                    inquirer.List(
                        "completed_book_main",
                        message = "COMPLETED BOOKS: Make a selection:",
                        choices = [
                            "View all the books you've finished.",

                            "<-- Go Back"
                        ]
            
                    )
                ]



        print('''

+++ !!!Welcome to GooderReads!!! +++

      ''')
    main_menu()

if __name__ == "__main__":
    main()

