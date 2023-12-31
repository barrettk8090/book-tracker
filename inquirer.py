# from sqlalchemy import Column, String, Integer, create_engine
# from sqlalchemy.orm import Session, declarative_base, validates
from models import *
import inquirer

#If this doesnt work be sure to comment back create engine at the bottom of models.oy

engine = create_engine('sqlite:///bookshelf.db')
Base.metadata.create_all(engine)

def main(): 
    with Session(engine) as session:
        #Main menu
        def main_menu():
            questions = [
                #Tried to copy the format that Sky had in Grtocery Lister but i was using their inquierer.List -- tried to change to Bookshelf but i have no idea whats happening so need to figure this out tomorrow 
                inquirer.Bookshelf(
                    "main_menu",
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
            if response("main_menu") ==  "View all the books on your Bookshelf":
                pass
            elif response("main_menu") == "View or edit the books in your 'Want to Read' list":
                pass
            elif response("main_menu") == "View or edit the books you're 'Currently Reading'":
                pass
            elif response("main_menu") == "View all of your completed books":
                pass
            else:
                exit()

        print('''

+++ !!!Welcome to GooderReads!!! +++

      ''')
        main_menu()

if __name__ == "__main__":
    main()
