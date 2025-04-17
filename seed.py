from app import create_app, db
from app.models import Book

app = create_app()

with app.app_context():
    db.create_all()

    if Book.query.count() == 0:
        books = [
            Book(title="1984", author="George Orwell", description="A dystopian novel."),
            Book(title="To Kill a Mockingbird", author="Harper Lee", description="Justice in the Deep South."),
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald", description="American dream and disillusionment."),
            Book(title="Pride and Prejudice", author="Jane Austen", description="Romance and social status."),
            Book(title="The Catcher in the Rye", author="J.D. Salinger", description="Teen rebellion and identity."),
            Book(title="Moby-Dick", author="Herman Melville", description="Whale hunting and obsession."),
            Book(title="The Hobbit", author="J.R.R. Tolkien", description="Fantasy and adventure."),
            Book(title="Brave New World", author="Aldous Huxley", description="Future society and control."),
            Book(title="Jane Eyre", author="Charlotte Brontë", description="Gothic romance and independence."),
            Book(title="Fahrenheit 451", author="Ray Bradbury", description="Book burning and censorship."),
        ]
        db.session.bulk_save_objects(books)
        db.session.commit()
        print("Seeded 10 books successfully!")
    else:
        print("Books already exist.")
