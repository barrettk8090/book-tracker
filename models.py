from sqlalchemy import Column, Integer, String, create_engine, func, ForeignKey
from sqlalchemy.orm import Session, declarative_base, validates

Base = declarative_base()

# Consider adding an author table? An author can have many books but we'll assume a book can only have one author
# Test add
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


engine = create_engine('sqlite:///bookshelf.db')

