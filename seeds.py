from models import *

if __name__ == '__main__':
    Bookshelf.__table__.drop(engine)
    WantToRead.__table__.drop(engine)
    CurrentlyReading.__table__.drop(engine)
    CompletedBook.__table__.drop(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:


        #Function for easily adding a book to your currently reading list.
        def add_currently_reading_book(session, title, author, description, page_count, current_page):
            bookshelf = Bookshelf()
            session.add(bookshelf)
            session.commit()

            currentbook = CurrentlyReading(
                book_title = title,
                book_author = author,
                book_description = description, 
                page_count = page_count,
                current_page = current_page,
                bookshelf_id = bookshelf.id
            )

            session.add(currentbook)
            session.commit()

        # Function for easily adding a book to your completed book pile.
        def add_completed_book(session, title, author, description, page_count, rating, review,):
            bookshelf = Bookshelf()
            session.add(bookshelf)
            session.commit()

            completedbook = CompletedBook(
                book_title = title,
                book_author = author,
                book_description = description,
                page_count = page_count,
                star_rating = rating,
                personal_review = review,
                bookshelf_id = bookshelf.id
            )

            session.add(completedbook)
            session.commit()

        add_currently_reading_book(session, "Hyperion", "Dan Simmons", "A few voyagers travel to Hyperion to solve a great cosmic mystery", 483, 291)
        add_currently_reading_book(session, "Why We Sleep", "Dan Simmons", "Neuroscientist and sleep expert Matthew Walker provides a revolutionary exploration of sleep, explaining how it affects every aspect of our physical and mental well-being.", 368, 250)

        add_completed_book(session, "The Three Body Problem", "Liu Cixin", "The people of Earth begin a friendly conversation with aliens!", 472, 5, "Loved this book and all the rest of the trilogy!")

        # bookshelf = Bookshelf()
        # session.add(bookshelf)
        # session.commit()

        # b1 = CurrentlyReading(
        # book_title = "Hyperion",
        # book_author = "Dan Simmons",
        # book_description = "A few voyagers travel to Hyperion to solve a great cosmic mystery",
        # page_count = 483,
        # current_page = 291,
        # bookshelf_id = bookshelf.id
        # )

        # bookshelf2 = Bookshelf()
        # session.add(bookshelf2)
        # session.commit()

        # b2 = CurrentlyReading(
        #     book_title = "Why We Sleep",
        #     book_author = "Matthew Walker",
        #     book_description = "Neuroscientist and sleep expert Matthew Walker provides a revolutionary exploration of sleep, explaining how it affects every aspect of our physical and mental well-being.",
        #     page_count = 368,
        #     current_page = 250,
        #     bookshelf_id = bookshelf2.id
        # )
     
        # session.add_all([b1, b2])
        # session.commit()

        # currently_reading_books = bookshelf.currently_reading_connection
        # for book in currently_reading_books:
        #     print(book.book_title)

