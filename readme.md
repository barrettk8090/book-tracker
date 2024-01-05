# GooderReads

Welcome to GooderReads! This app is built in Python, with SQLAlchemy and the Inquirer library. This CLI app serves to replicate some of the core functionality of Goodreads, along with some fun additions and stats. The main functions are viewing, adding, editing/updating, removing, and moving books in three lists: Want to Read books, Currently Reading books, and Completed books.

## Running GooderReads

To run the CLI program, download or clone the file and the navigate to the project directory. In the terminal, run

```
pipenv install
pipenv shell
python3 lib/app.py
```

Once the program is running, use the arrow keys in the main menu to navigate through the selection choices. User ENTER to select a choice, and add additional input when prompted.

Try experimenting with:

- adding a new book to your Want to Read list.
- moving a book from Want to Read to Currently Reading.
- updating the progress on a book you're Currently Reading (e.g. updating the current page you're on)
- marking a Currently Reading book as Complete.
- viewing some stats on your Completed Books.
- deleting/removing all the sample books and starting fresh with your own list!
