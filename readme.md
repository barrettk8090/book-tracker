# GooderReads

Initializing ReadMe

To Dos
[ ] Add edit functionality to all shelves (e.g. edit a rating, edit an author, etc.)

> > First you need to query who you want to edit and then you can set a change to one of the columns. E.g. book = session.query(Bookshelf).filter(Bookshelf.id == 12).first()
> > book.title = "New Title"

[X] Config/confirm structure of bookshelves
[ ] Add validation to everything
@validates('email')
def validate_email(self, key, value):
if type(value) is str and "@" in value:
return value
else:
raise ValueError("Not valid email)

[ ] Add genres field

[ ] Add columns and auto widths to returns (e.g. when learning plain SQL there was a way to show the table headers HEADERS ON and see things in a prettier way than just a list)

[ ] Get the total number of pages that you've read, either in total or as part of a specific year that you read them.

[ ] Add a new bookshelf type, make that work somehow, and get a join table cookin!

Stretch
[ ] Add login/user functionality so that there can be multiple people accounts who have bookshelves
[ ] Connect to OpenLibrary API to allow for searching(?) by a book title or author and get the description and other info so that you can automatically enter that information iunto the table without having to type anything. Query that database
[ ] For currently reading books, when you type in the current page number and it gets compared to the total number of pages to show you the percentage of completion, have it also show a progress bar of how far along you are.
https://www.makeuseof.com/python-cli-progress-bar-tqdm/
https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
[ ] Add colors https://pypi.org/project/cli-color-py/
