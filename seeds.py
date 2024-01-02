from models import *

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

    session.add_all([cr_shelf,wtr_shelf,completed_shelf])
    session.commit()
    session.add(b1)
    session.commit()

