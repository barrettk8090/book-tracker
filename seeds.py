from models import *

# These may need to change based on how the tables get restructured to match the reqyuirements for the project
if __name__ == '__main__':
    Bookshelf.__table__.drop(engine)
    WantToRead.__table__.drop(engine)
    CurrentlyReading.__table__.drop(engine)
    CompletedBooks.__table__.drop(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:

        b1 = Bookshelf(
        book_title = "Hyperion",
        book_author = "Dan Simmons",
        book_description = "A few voyagers travel to Hyperion to solve a great cosmic mystery",
        page_count = 500
        )

        b2 = Bookshelf(
            book_title = "Misery",
            book_author = "Stephen King",
            book_description = "Crazy lady tortures novelist.",
            page_count = 300
        )
    session.add_all([b1, b2])
    session.commit()

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