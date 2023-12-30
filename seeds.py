from models import *

# These may need to change based on how the tables get restructured to match the reqyuirements for the project
if __name__ == '__main__':
    Bookshelf.__table__.drop(engine)
    WantToRead.__table__.drop(engine)
    CurrentlyReading.__table__.drop(engine)
    CompletedBooks.__table__.drop(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:

        bookshelf = Bookshelf()
        session.add(bookshelf)
        session.commit()

        b1 = CurrentlyReading(
        book_title = "Hyperion",
        book_author = "Dan Simmons",
        book_description = "A few voyagers travel to Hyperion to solve a great cosmic mystery",
        page_count = 483,
        current_page = 291,
        bookshelf_id = bookshelf.id
        )

        # b2 = Bookshelf(
        #     book_title = "Misery",
        #     book_author = "Stephen King",
        #     book_description = "Crazy lady tortures novelist.",
        #     page_count = 300
        # )
        session.add(b1)
        session.commit()

        currently_reading_books = bookshelf.currently_reading_connection
        for book in currently_reading_books:
            print(book.book_title)

    #    all_books = session.query(Bookshelf).all()
    #     first_book = session.query(Bookshelf).filter(Bookshelf.id ==1).first()
    #     second_book = session.query(Bookshelf).filter(Bookshelf.id == 2).first()
    #     # print(all_books)
    #     print(first_book)
    #     print(second_book)
    #     second_book.book_description = "Crazy lady brtually tortures novelist but he ends up escaping."
    #     session.add(second_book)
    #     session.commit()
    #     print(second_book)