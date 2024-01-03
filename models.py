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

    @validates("name", "description")
    def validate_name_desc(self, key, value):
        if type(value) is str and 3<len(value):
            return value
        else:
            raise ValueError(f"Sorry, that is not a valid {value}")

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key = True)
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

    @validates("title", "author")
    def validate_title_author(self, key, value):
        if type(value) is str and 0<len(value):
            return value
        else:
            raise ValueError(f"Sorry, but you must enter a {value}. Please try again.")
        
    @validates("page_count")
    def validate_page_count(self, key, value):
        if type(value) is int and 0 < value:
            return value
        elif type(value) is str and 0<=len(value):
            return int(value)
        else:
            raise ValueError(f"Please enter a value for page count so that we can track your progress later on.")
    
    @validates("pages_read")
    def validate_pages_read(self, key, value):
        if type(value) is int and 0<=value:
            return value
        elif type(value) is str and 0<=len(value):
            return int(value)
        elif type(value) is str and value == "":
            value = 0 
            return value
        else:
            raise ValueError(f"Please enter a valid {value}. If you haven't read any pages yet, you can enter 0 or leave the field blank, WITHOUT any spaces, please.")
        
    #strech goal: validate type--> if type text already exists in table return value. If it doesnt exist yet, raise an error and ask if user wants to create a new type first. Then go thru type recreation and start over current process.
    @validates("type")
    def validate_type(self, key, value):
        if type(value) is str and 0<len(value):
            return value
        else:
            raise ValueError(f"Please enter a valid {value}")
        
    #stretch - add float w one decimal place eg. 4.5 2.7
    @validates("star_rating")
    def validate_star_rating(self, key, value):
        if type(value) is int and 0<=value<=5 or value == None:
            return value
        else:
            raise ValueError(f"Please enter a {value} that is between 0 and 5 with no decimal places.")

    @validates("personal_review")
    def validate_personal_rev(self, key, value):
        if type(value) is str and 1<len(value) or value == None:
            return value
        else:
            raise ValueError(f"Please enter a {value} that's longer than one character.")
    

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
