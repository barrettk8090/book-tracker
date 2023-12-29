from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()

# Consider adding an author table? An author can have many books but we'll assume a book can only have one author

class Bookshelf(Base):
    __tablename__ = "bookshelf" 
    id = Column(Integer, primary_key = True)
    book_title = Column(String, nullable = False)
    book_author = Column(String, nullable = False)
    book_description = Column(String)
    page_count = Column(Integer)
    # date_started = Column()
    # date_finished = Column()

    def __repr__(self):
        return f'{self.book_title} by author {self.book_author}. Description: {self.book_description}. Page count {self.page_count}.'

class WantToRead(Base):
    __tablename__ = "want to read"
    id = Column(Integer, primary_key = True)
    book_title = Column(String)
    book_author = Column(String)
    book_description = Column(String)
    page_count = Column(Integer)

class CurrentlyReading(Base):
    __tablename__ = "currently reading"
    id = Column(Integer, primary_key = True)
    book_title = Column(String)
    book_author = Column(String)
    book_description = Column(String)
    page_count = Column(Integer)
    current_page = Column(Integer)

class CompletedBooks(Base):
    __tablename__ = "completed"
    id = Column(Integer, primary_key = True)
    book_title = Column(String)
    book_author = Column(String)
    book_description = Column(String)
    page_count = Column(Integer)
    star_rating = Column(Integer)
    personal_review = Column(String)

if __name__ == '__main__':

    engine = create_engine('sqlite:///bookshelf.db')
    Base.metadata.create_all(engine)

    with Session(engine) as session:
    #     b1 = Bookshelf(
    #         book_title = "Hyperion",
    #         book_author = "Dan Simmons",
    #         book_description = "A few voyagers travel to Hyperion to solve a great cosmic mystery",
    #         page_count = 500
    #     )

    #     b2 = Bookshelf(
    #         book_title = "Misery",
    #         book_author = "Stephen King",
    #         book_description = "Crazy lady tortures novelist.",
    #         page_count = 300
    #     )
    # session.add(b2)
    # session.commit()
        all_books = session.query(Bookshelf).all()
        first_book = session.query(Bookshelf).filter(Bookshelf.id ==1).first()
        second_book = session.query(Bookshelf).filter(Bookshelf.id == 2).first()
        # print(all_books)
        print(first_book)
        print(second_book)
        second_book.book_description = "Crazy lady brtually tortures novelist but he ends up escaping."
        session.add(second_book)
        session.commit()
        print(second_book)