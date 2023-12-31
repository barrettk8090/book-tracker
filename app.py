#Our main program
from models import * 

print('''
             
++++++++++++ WELCOME TO GOODER READS ++++++++++++

''')

if __name__ == '__main__':
    with Session(engine) as session:

        entry_selection = input(
'''

Welcome to your bookshelf! What would you like to do today?
                                
1. View all the books on your bookshelf.
2. View or edit your Want To Read list.
3. View or edit the books on your Currently Reading list.
4. View or edit the books on your Completed Books list. 
'''
                                )
        if entry_selection == "1":
            print (f'Alright, here\'s a list of all the books you currently have on your bookshelf: {session.query(Bookshelf).all}')
        if entry_selection == "2":
            wtr_master = input(
'''
+++ Want to Read +++
1. VIEW all the books in your want to read list.
2. EDIT a book on your want to read list.
3. ADD a book to your want to read list.
4. MOVE a book from your want to read list to your Currently Reading list.
5. MOVE a book from your want to read list to your Completed Books list. 
6. <-- Go back

'''
                                  )
            if wtr_master == "1":
                print(session.query(WantToRead).all())
            if wtr_master == "2":
                

    


#        first_selection =  input('''
# What would you like to do?
              
# 1. Add a book to your Want to Read shelf
# 2. Add a book to your currently reading list
# 3. Add a book to your completed books pile
# 4. View your entire bookshelf
# 5. View a list of all authors on your bookshelf & their corresponding books.
# ''')
       
#     #    Prompt user for information regarding a book they want to add to their Want to Read list.
#        if first_selection == "1":
#           i1 = input("What is the title of the book you want to read?: ")
#           i2 = input(f"Who is the author of {i1}?: ")
#           i3 = input(f"Write a brief book description for {i1}: ")
#           i4 = input(f"Type the number of pages that are in {i1}: ")
#           wtr = WantToRead(
#              book_title = i1,
#              book_author = i2,
#              book_description = i3,
#              page_count = i4
#           )
#           session.add(wtr)
#           session.commit()
#           print(f"Awesome! I've added the book, {i1}, to your Want To Read list! It can also be found on your master bookshelf. ")
       

#        # Display a list of all the books a user has on their bookself. 
#        elif first_selection == "4":
#         all_books = session.query(Bookshelf).all()
#         print(all_books)