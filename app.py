#Our main program
from models import * 

if __name__ == '__main__':
    with Session(engine) as session:
       first_selection =  input('''
What would you like to do?
              
1. Add a book to your Want to Read shelf
2. Add a book to your currently reading list
3. Add a book to your completed books pile
4. View your entire bookshelf
5. View a list of all authors on your bookshelf & their corresponding books.
''')
       
    #    Prompt user for information regarding a book they want to add to their Want to Read list.
       if first_selection == "1":
          i1 = input("What is the title of the book you want to read?: ")
          i2 = input(f"Who is the author of {i1}?: ")
          i3 = input(f"Write a brief book description for {i1}: ")
          i4 = input(f"Type the number of pages that are in {i1}: ")
          wtr = WantToRead(
             book_title = i1,
             book_author = i2,
             book_description = i3,
             page_count = i4
          )
          session.add(wtr)
          session.commit()
          print(f"Awesome! I've added the book, {i1}, to your Want To Read list! It can also be found on your master bookshelf. ")
       

       # Display a list of all the books a user has on their bookself. 
       elif first_selection == "4":
        all_books = session.query(Bookshelf).all()
        print(all_books)