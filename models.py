from sqlalchemy import Column, Integer, String, create_engine, func, ForeignKey
from sqlalchemy.orm import Session, declarative_base, validates, relationship

Base = declarative_base()

# Consider adding an author table? An author can have many books but we'll assume a book can only have one author
# Test add
class Bookshelf(Base):
    __tablename__ = "bookshelf" 
    id = Column(Integer, primary_key = True)
    name = Column(String)
    description = Column(String)
    book_connection = relationship('Book', back_populates = "bookshelf_connection")


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key= True)
    title = Column(String, nullable = False)
    author = Column(String, nullable = False)
    description = Column(String)
    page_count = Column(Integer)
    pages_read = Column(Integer)
    type = Column(String)
    star_rating = Column(Integer)
    personal_review = Column(String)
    bookshelf_id = Column(ForeignKey('bookshelf.id'))
    bookshelf_connection = relationship('Bookshelf', back_populates="book_connection")

    def __repr__(self):
        return f'''
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        +    {self.title.upper()} by {self.author}.                    
        +    Book description: {self.description}                      
        +    Pages: {self.page_count}                                  
        +    Type: {self.type}                                         
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        '''

engine = create_engine('sqlite:///bookshelf.db')
