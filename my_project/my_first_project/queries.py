books = Book.objects.all()
for book in books:
    print(book.title, book.author)


reviews = Review.objects.all()
for review in reviews:
    print(review.reviewer_name, review.review_text)


from datetime import date

recent_books = Book.objects.filter(publication_date__gt=date(2000, 1, 1))
for book in recent_books:
    print(book.title, book.publication_date)



high_rating_reviews = Review.objects.filter(rating=5)
for review in high_rating_reviews:
    print(review.reviewer_name, review.book.title, review.rating)



author_books = Book.objects.filter(author='George Orwell')
for book in author_books:
    print(book.title, book.author)


book = Book.objects.get(title='1984')
reviews = Review.objects.filter(book=book)
for review in reviews:
    print(review.reviewer_name, review.review_text)



from django.db.models import Avg

book = Book.objects.get(title='1984')
average_rating = Review.objects.filter(book=book).aggregate(Avg('rating'))
print(f'Average rating for 1984: {average_rating["rating__avg"]}')



books_with_pages = Book.objects.filter(pages__gt=200)
for book in books_with_pages:
    print(book.title, book.pages)



from django.db.models import Max

latest_reviews = Review.objects.values('book').annotate(latest_review_date=Max('review_date')).order_by('book')
for review in latest_reviews:
    book = Book.objects.get(id=review['book'])
    latest_review = Review.objects.get(book=book, review_date=review['latest_review_date'])
    print(f'Latest review for {book.title} by {latest_review.reviewer_name}: {latest_review.review_text}')



books_with_high_rating_reviews = Book.objects.filter(reviews__rating=5).distinct()
for book in books_with_high_rating_reviews:
    print(book.title)



from django.db.models import Count

reviews_grouped_by_rating = Review.objects.values('rating').annotate(count=Count('id')).order_by('-count')
for review_group in reviews_grouped_by_rating:
    print(f'Rating: {review_group["rating"]}, Count: {review_group["count"]}')



from django.db.models import Count

most_reviewed_book = Book.objects.annotate(review_count=Count('reviews')).order_by('-review_count').first()
print(f'Most reviewed book: {most_reviewed_book.title} with {most_reviewed_book.review_count} reviews')



books_with_no_reviews = Book.objects.annotate(review_count=Count('reviews')).filter(review_count=0)
for book in books_with_no_reviews:
    print(book.title)



from django.db.models import Avg

average_ratings = Book.objects.annotate(average_rating=Avg('reviews__rating')).order_by('-average_rating')
for book in average_ratings:
    print(f'Book: {book.title}, Average Rating: {book.average_rating}')
