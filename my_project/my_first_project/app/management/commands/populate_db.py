from django.core.management.base import BaseCommand
from app.models import Book, Review

class Command(BaseCommand):
    help = 'Populate the database with sample Book and Review data'

    def handle(self, *args, **kwargs):
        # Sample books
        books = [
            {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'publication_date': '1925-04-10', 'isbn': '9780743273565', 'pages': 180},
            {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'publication_date': '1960-07-11', 'isbn': '9780061120084', 'pages': 281},
            {'title': '1984', 'author': 'George Orwell', 'publication_date': '1949-06-08', 'isbn': '9780451524935', 'pages': 328},
            {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'publication_date': '1813-01-28', 'isbn': '9781503290563', 'pages': 279},
            {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'publication_date': '1951-07-16', 'isbn': '9780316769488', 'pages': 214}
        ]

        # Create books
        for book_data in books:
            book, created = Book.objects.get_or_create(**book_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created book: {book.title}'))

        # Sample reviews
        reviews = [
            {'book': Book.objects.get(isbn='9780743273565'), 'review_text': 'A masterpiece of American literature.', 'rating': 5, 'reviewer_name': 'John Doe'},
            {'book': Book.objects.get(isbn='9780061120084'), 'review_text': 'A profound novel with deep themes.', 'rating': 5, 'reviewer_name': 'Jane Smith'},
            {'book': Book.objects.get(isbn='9780451524935'), 'review_text': 'A chilling dystopian story.', 'rating': 4, 'reviewer_name': 'Alice Johnson'},
            {'book': Book.objects.get(isbn='9781503290563'), 'review_text': 'A classic romance with witty commentary.', 'rating': 4, 'reviewer_name': 'Bob Brown'},
            {'book': Book.objects.get(isbn='9780316769488'), 'review_text': 'A thought-provoking coming-of-age story.', 'rating': 4, 'reviewer_name': 'Carol White'}
        ]

        # Create reviews
        for review_data in reviews:
            review, created = Review.objects.get_or_create(**review_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created review by {review.reviewer_name} for {review.book.title}'))
