from sqlalchemy import Column, Integer, String, create_engine, func, ForeignKey
from sqlalchemy.orm import Session, declarative_base, validates, relationship

Base = declarative_base()

# Consider adding an author table? An author can have many books but we'll assume a book can only have one author
# Test add
class Bookshelf(Base):
    __tablename__ = "bookshelf" 
    id = Column(Integer, primary_key = True)
    want_to_read_connection = relationship('WantToRead', back_populates="bookshelf_connection")
    currently_reading_connection = relationship('CurrentlyReading', back_populates="bookshelf_connection")
    completed_books_connection = relationship('CompletedBook', back_populates="bookshelf_connection")

class WantToRead(Base):
    __tablename__ = "want to read"
    id = Column(Integer, primary_key = True)
    book_title = Column(String)
    book_author = Column(String)
    book_description = Column(String)
    page_count = Column(Integer)
    bookshelf_id = Column(ForeignKey('bookshelf.id'))
    bookshelf_connection = relationship('Bookshelf', back_populates="want_to_read_connection")

class CurrentlyReading(Base):
    __tablename__ = "currently reading"
    id = Column(Integer, primary_key = True)
    book_title = Column(String)
    book_author = Column(String)
    book_description = Column(String)
    page_count = Column(Integer)
    current_page = Column(Integer)
    bookshelf_id = Column(ForeignKey('bookshelf.id'))
    bookshelf_connection = relationship('Bookshelf', back_populates="currently_reading_connection")

class CompletedBook(Base):
    __tablename__ = "completed"
    id = Column(Integer, primary_key = True)
    book_title = Column(String)
    book_author = Column(String)
    book_description = Column(String)
    page_count = Column(Integer)
    star_rating = Column(Integer)
    personal_review = Column(String)
    bookshelf_id = Column(ForeignKey('bookshelf.id'))
    bookshelf_connection = relationship('Bookshelf', back_populates="completed_books_connection")


engine = create_engine('sqlite:///bookshelf.db')

