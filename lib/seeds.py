from models.models import *

if __name__ == '__main__':
    Bookshelf.__table__.drop(engine)
    Book.__table__.drop(engine)
    Base.metadata.create_all(engine)


with Session(engine) as session:

    cr_shelf = Bookshelf(
        name = "Currently Reading",
        description = "A list of books that I'm currently reading"
    )
    
    wtr_shelf = Bookshelf(
        name = "Want to Read",
        description = "A list of books that I eventually want to read."
    )

    completed_shelf = Bookshelf(
        name = "Completed Books",
        description = "Books I've finished."
    )

    b1 = Book(
        title = "Hyperion",
        author = "Dan Simmons",
        description = "A few voyagers travel to Hyperion to solve a great cosmic mystery",
        page_count = 483,
        pages_read = 414,
        type = "Currently Reading",
        star_rating = 5,
        personal_review = "Really enjoying it!",
        bookshelf_id = 1
    )

    b2 = Book(
        title = "Why We Sleep",
        author = "Matthew Walker",
        description = "Neuroscientist and sleep expert Matthew Walker provides a revolutionary exploration of sleep, explaining how it affects every aspect of our physical and mental well-being.",
        page_count = 368,
        pages_read = 250,
        type = "Currently Reading",
        star_rating = None,
        personal_review = None,
        bookshelf_id = 1
    )

    b3 = Book(
        title = "Wool",
        author = "Hugh Howey",
        description = "Thousands of them have lived underground. They've lived there so long, there are only legends about people living anywhere else.",
        page_count = 594,
        pages_read = 0,
        type = "Want To Read",
        star_rating = None,
        personal_review = None,
        bookshelf_id = 2
    )

    b4 = Book(
        title = "Leviathan Wakes",
        author = "James S.A. Corey",
        description = "Humanity has colonized the solar system—Mars, the Moon, the Asteroid Belt and beyond—but the stars are still out of our reach.",
        page_count = 592,
        pages_read = 0,
        type = "Want To Read",
        star_rating = None,
        personal_review = None,
        bookshelf_id = 2
    )

    b5 = Book(
        title = "The Three Body Problem",
        author = "Liu Cixin",
        description = "Set against the backdrop of China's Cultural Revolution, a secret military project sends signals into space to establish contact with aliens.",
        page_count = 472,
        pages_read = 472,
        type = "Completed",
        star_rating = 5,
        personal_review = "Such a wild start to the trilogy",
        bookshelf_id = 3
    )

    b6 = Book(
        title = "The Dark Forest",
        author = "Liu Cixin",
        description = "This is the second novel in Remembrance of Earths Past, the near-future trilogy written by China's multiple-award-winning science fiction author, Cixin Liu.",
        page_count = 512,
        pages_read = 512,
        type = "Completed",
        star_rating = 5,
        personal_review = "This book rocked and one of the end sequences is incredible.",
        bookshelf_id = 3
    )

    b7 = Book(
        title = "The Dark Forest",
        author = "Liu Cixin",
        description = "Half a century after the Doomsday Battle, the uneasy balance of Dark Forest Deterrence keeps the Trisolaran invaders at bay.",
        page_count = 604,
        pages_read = 604,
        type = "Completed",
        star_rating = 5,
        personal_review = "A super-solid, far-out ending to the trilogy.",
        bookshelf_id = 3
    )

    b8 = Book(
        title = "The Deluge",
        author = "Stephen Markley",
        description = "In the first decades of the 21st century, the world is convulsing, its governments mired in gridlock while a patient but unrelenting ecological crisis looms.",
        page_count = 896,
        pages_read = 0,
        type = "Want To Read",
        star_rating = None,
        personal_review = None,
        bookshelf_id = 2
    )

    b9 = Book(
        title = "Where I End",
        author = "Sophie White",
        description = "Aoileann desperately wants a family, and when Sarah and her three young children move to the island, Aoileann finds a focus for her relentless love.",
        page_count = 232,
        pages_read = 0,
        type = "Want To Read",
        star_rating = None,
        personal_review = None,
        bookshelf_id = 2
    )

    b10 = Book(
        title = "Ancillary Justice",
        author = "Anne Leckie",
        description = "On a remote, icy planet, the soldier known as Breq is drawing closer to completing her quest.",
        page_count = 386,
        pages_read = 0,
        type = "Want To Read",
        star_rating = None,
        personal_review = None,
        bookshelf_id = 2
    )

    b11 = Book(
        title = "Demon Copperhead",
        author = "Barbara Kingsolver",
        description = "Set in the mountains of southern Appalachia, this is the story of a boy born to a teenaged single mother in a single-wide trailer...",
        page_count = 560,
        pages_read = 560,
        type = "Completed",
        star_rating = 5,
        personal_review = "Great beach read. Sad!",
        bookshelf_id = 3
    )

    b12 = Book(
        title = "The Way of Kings",
        author = "Brandon Sanderson",
        description = "A richly imagined epic set in a world relentlessly blasted by awesome tempests, where emotions take on physical form, and terrible secrets hide deep within the rocky landscape.",
        page_count = 1258,
        pages_read = 1258,
        type = "Completed",
        star_rating = 5,
        personal_review = "My first real attempt at reading fantasy and then got sucked in for thousands more pages.",
        bookshelf_id = 3
    )
    

    


    session.add_all([cr_shelf,wtr_shelf,completed_shelf])
    session.commit()
    session.add_all([b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12])
    session.commit()

