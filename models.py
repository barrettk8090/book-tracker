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

    def __repr__(self):
        want_to_read_books = ", ".join([book.book_title for book in self.want_to_read_connection])
        currently_reading_books = ", ".join([book.book_title for book in self.currently_reading_connection])
        completed_books = ", ".join([book.book_title for book in self.completed_books_connection])

        return f"Bookshelf(id={self.id}), WantToRead =[{want_to_read_books}], CurrentlyReading=[{currently_reading_books}], Completed=[{completed_books}]"


class WantToRead(Base):
    __tablename__ = "want to read"
    id = Column(Integer, primary_key = True)
    shelf_type = Column(String, default = "Want to Read")
    book_title = Column(String, nullable = False)
    book_author = Column(String, nullable = False)
    book_description = Column(String)
    page_count = Column(Integer)
    bookshelf_id = Column(ForeignKey('bookshelf.id'))
    bookshelf_connection = relationship('Bookshelf', back_populates="want_to_read_connection")

    @validates("book_title", "book_author")
    def validates_title_and_author(self, key, value):
        if type(value) is str and 0<len(value):
            return value
        else:
            raise ValueError(f'Sorry, that isnt a valid {value}')
        #Working, but value isn't getting returned, need to fix
        
    @validates("page_count")
    def validates_page_count(self, key, value):
        if 0 < value and value <= 3000:
            return value
        elif value > 3001:
            raise ValueError("It looks like you're trying to add a book that's longer than 3000 pages. You'll never read that, so it hasn't been added to your Want To Read list.")
        else:
            raise ValueError("Please enter a page count between 2 and 3000 pages.")
    
    def __repr__(self):
        return f'{self.book_title}'

class CurrentlyReading(Base):
    __tablename__ = "currently reading"
    id = Column(Integer, primary_key = True)
    self_type = Column(String, default = "Currently Reading")
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
    self_type = Column(String, default= "Completed")
    book_title = Column(String)
    book_author = Column(String)
    book_description = Column(String)
    page_count = Column(Integer)
    star_rating = Column(Integer)
    personal_review = Column(String)
    bookshelf_id = Column(ForeignKey('bookshelf.id'))
    bookshelf_connection = relationship('Bookshelf', back_populates="completed_books_connection")


engine = create_engine('sqlite:///bookshelf.db')

