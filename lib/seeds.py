from models.models import *

if __name__ == '__main__':
    Bookshelf.__table__.drop(engine)
    Book.__table__.drop(engine)
    Base.metadata.create_all(engine)


with Session(engine) as session:

    cr_shelf = Bookshelf(
        name = "Currently Reading",
        description = "A list of books that I'm currently reading"
    )
    
    wtr_shelf = Bookshelf(
        name = "Want to Read",
        description = "A list of books that I eventually want to read."
    )

    completed_shelf = Bookshelf(
        name = "Completed Books",
        description = "Books I've finished."
    )

    b1 = Book(
        title = "Hyperion",
        author = "Dan Simmons",
        description = "A few voyagers travel to Hyperion to solve a great cosmic mystery",
        page_count = 483,
        pages_read = 340,
        type = "Currently Reading",
        star_rating = 5,
        personal_review = "Really enjoying it!",
        bookshelf_id = 1
    )

    b2 = Book(
        title = "Why We Sleep",
        author = "Matthew Walker",
        description = "Neuroscientist and sleep expert Matthew Walker provides a revolutionary exploration of sleep, explaining how it affects every aspect of our physical and mental well-being.",
        page_count = 368,
        pages_read = 250,
        type = "Currently Reading",
        star_rating = None,
        personal_review = None,
        bookshelf_id = 1
    )

    b3 = Book(
        title = "Wool",
        author = "Hugh Howey",
        description = "Thousands of people live underground and no one knows why.",
        page_count = 594,
        pages_read = 0,
        type = "Want To Read",
        star_rating = None,
        personal_review = None,
        bookshelf_id = 2
    )

    b4 = Book(
        title = "Leviathan Wakes",
        author = "James S.A. Corey",
        description = "I'm honestly not entirely sure but I've heard its good.",
        page_count = 592,
        pages_read = 0,
        type = "Want To Read",
        star_rating = None,
        personal_review = None,
        bookshelf_id = 2
    )

    b5 = Book(
        title = "The Three Body Problem",
        author = "Liu Cixin",
        description = "The people of Earth begin a friendly conversation with aliens!",
        page_count = 472,
        pages_read = 472,
        type = "Completed",
        star_rating = 5,
        personal_review = "Completely fantastic",
        bookshelf_id = 3
    )

    b6 = Book(
        title = "The Dark Forest",
        author = "Liu Cixin",
        description = "The people of earth realize that the aliens are actually not friendly at all and want to kill everyone.",
        page_count = 512,
        pages_read = 512,
        type = "Completed",
        star_rating = 5,
        personal_review = "This book rocked and one of the end sequences is incredible. Love the idea of the dark forest.",
        bookshelf_id = 3
    )


    session.add_all([cr_shelf,wtr_shelf,completed_shelf])
    session.commit()
    session.add_all([b1,b2,b3,b4,b5,b6])
    session.commit()

