# GooderReads

Welcome to GooderReads! This app is built in Python, with SQLAlchemy and the Inquirer library. This CLI app serves to replicate some core functionality of Goodreads, along with some fun additions and stats. The main functions are viewing, adding, editing/updating, removing, and moving books in three lists: Want to Read books, Currently Reading books, and Completed books.

## Running GooderReads

To run the CLI program, download or clone the file and the navigate to the project directory. In the terminal, run
//pipenv install
//pipenv shell
//python3 lib/app.py

Once the program is running, use the arrow keys in the main menu to navigate through the selection choices. User ENTER to select a choice, and add input when prompted.

Try experimenting with:
• adding a new book to your Want to Read list.
• moving a book from Want to Read to Currently Reading.
• updating the progress on a book you're Currently Reading (e.g. updating the current page you're on)
• viewing some stats on your Completed Books.

[ ] Add genres field

Stretch
[ ] Add login/user functionality so that there can be multiple people accounts who have bookshelves
[ ] Connect to OpenLibrary API to allow for searching(?) by a book title or author and get the description and other info so that you can automatically enter that information iunto the table without having to type anything. Query that database
[ ] For currently reading books, when you type in the current page number and it gets compared to the total number of pages to show you the percentage of completion, have it also show a progress bar of how far along you are.
https://www.makeuseof.com/python-cli-progress-bar-tqdm/
https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
[ ] Add colors https://pypi.org/project/cli-color-py/
