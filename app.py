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
            main_menu()


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

        #stretch - fix with loops --> Starter code below VVVV
                # could ALSO change this to be like... "please type the book title you want to edit". Probs a better approach than the below
        def edit_wtr_details_menu():
            # all_wtr = session.query(Book).filter(Book.bookshelf_id == 2).all()
            # i = 0 
            # while i < len(all_wtr):
                
            #     questions = [
            #         inquirer.List(
            #             "edit_wtr_details_menu",
            #             message = "Which book do you want to edit?",
            #             choices = [
            #                 f"{all_wtr[i].title}",
            #                 "<-- Go Back"
            #             ]
            #         )
            #     ]
                
            #     i += 1
            # response = inquirer.prompt(questions)
            all_wtr = session.query(Book).filter(Book.bookshelf_id == 2).all()
            questions = [
                    inquirer.List(
                        "edit_wtr_details_menu",
                        message = "Which book do you want to edit?",
                        choices = [
                            f"{all_wtr[0].title}",
                            f"{all_wtr[1].title}",
                            f"{all_wtr[2].title}",
                            # f"{all_wtr[3].title}",
                            # f"{all_wtr[4].title}",
                            "<-- Go Back"
                        ]
                    )
                ]
            response = inquirer.prompt(questions)
            if response ["edit_wtr_details_menu"] == f"{all_wtr[0].title}":
                new_title = input("Confirm or edit the title of this book: ")
                new_author = input("Confirm or edit the authors name: ")
                new_description = input("Confirm or edit the book description: ")
                new_page_count = input("Confirm or edit the books page count: ")

                session.delete(all_wtr[0])

                all_wtr[0].title = new_title
                all_wtr[0].author = new_author
                all_wtr[0].description = new_description
                all_wtr[0].page_count = new_page_count

            
                session.add(all_wtr[0])
                session.commit()

                print(f"Great! I've modified that book in your Want to Read list. Here's the new book info:\n {all_wtr[0]}" )
                wtr_return_prompt()
            elif response ["edit_wtr_details_menu"] == f"{all_wtr[1].title}":
                new_title = input("Confirm or edit the title of this book: ")
                new_author = input("Confirm or edit the authors name: ")
                new_description = input("Confirm or edit the book description: ")
                new_page_count = input("Confirm or edit the books page count: ")

                session.delete(all_wtr[1])
                
                all_wtr[1].title = new_title
                all_wtr[1].author = new_author
                all_wtr[1].description = new_description
                all_wtr[1].page_count = new_page_count

            
                session.add(all_wtr[1])
                session.commit()

                print(f"Great! I've modified that book in your Want to Read list. Here's the new book info:\n {all_wtr[1]}" )
                wtr_return_prompt()
            elif response ["edit_wtr_details_menu"] == f"{all_wtr[2].title}":
                new_title = input("Confirm or edit the title of this book: ")
                new_author = input("Confirm or edit the authors name: ")
                new_description = input("Confirm or edit the book description: ")
                new_page_count = input("Confirm or edit the books page count: ")

                session.delete(all_wtr[2])
                
                all_wtr[2].title = new_title
                all_wtr[2].author = new_author
                all_wtr[2].description = new_description
                all_wtr[2].page_count = new_page_count

            
                session.add(all_wtr[2])
                session.commit()

                print(f"Great! I've modified that book in your Want to Read list. Here's the new book info:\n {all_wtr[2]}" )
                wtr_return_prompt()
            else:
                edit_wtr_menu()

        #delete a book from want to read 
        def del_wtr():
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
                print("Okay, that book has now been permanently deleted from your Want to Read list.")
                session.delete(book_del)
                session.commit()
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
            print(set(all_authors))
            wtr_return_prompt()

        def move_wtr():
            #should we maybe print a list of all the book titles here to make it easier to type?
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
                print(f"Thanks! {title_to_move} has been moved from your Want to Read list to your Currently Reading list.")
                print(book_move)
                wtr_return_prompt()
            else:
                wtr_main()


            #     print(book_move)
            #     print("Okay, that book has now been permanently deleted from your Want to Read list.")
            #     session.delete(book_del)
            #     session.commit()
            # else:
            #     wtr_main()







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
                view_cb()
                pass
            elif response["completed_main_menu"] == "Get cool stats on the books I've finished.":
                cool_cb_stats()
                pass
            elif response["completed_main_menu"] == "Edit a book on your completed list":
                #edit_cb()
                pass
            elif response["completed_main_menu"] == "Remove a book from your completed list.":
                #remove_cb
                pass
            else:
                main_menu()

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
            print("Here's a list of all the books you've finished reading:")
            all_cb = session.query(Book).filter(Book.bookshelf_id == 3).all()
            print(all_cb)

            cb_return_prompt()

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
                #calc_top_author()
                pass
            else:
                completed_main()

        def total_completed_books():
            all_cb = session.query(Book).filter(Book.bookshelf_id == 3).all()
            print(f"Altogether, you've read and finished {len(all_cb)} books!")
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
            print(f"In total, you have read {total_pages} pages!")
            cb_return_prompt()

        #calculate the author that has been read the most 
        def calc_top_author():
            pass
 
        print('''

+++ !!!Welcome to GooderReads!!! +++
               ___________
              /           \
              |            |
              |       ___
              |      |    \
              |            |
              |            |
              \____________/

      ''')
    main_menu()

if __name__ == "__main__":
    main()
