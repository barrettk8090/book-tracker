#Our main program
from models import * 

if __name__ == '__main__':
    with Session(engine) as session:
        input('''
What would you like to do?
              
>> Add a book to your Want to Read shelf
>> Add a book to your currently reading list
>> Add a book to your completed books pile
>> View your entire bookshelf
''')