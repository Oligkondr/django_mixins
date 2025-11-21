from django.test import TestCase
from datetime import date
from media.models import Movie, Book, AudioBook


# Create your tests here.
class MovieModelTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Movie1",
            creator="Creator1",
            publication_date=date(2025, 7, 16),
            duration=123,
            format="mp4"
        )

    # 1. Тест создания объекта Movie
    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Movie1")
        self.assertEqual(self.movie.creator, "Creator1")
        self.assertEqual(self.movie.duration, 123)
        self.assertEqual(self.movie.format, "mp4")
        self.assertIsNotNone(self.movie.id)

    # 2. Тест методов Movie
    def test_movie_methods(self):
        description = self.movie.get_description()
        self.assertIn("Фильм 'Movie1' режиссера Creator1", description)

        trailer_text = self.movie.play_trailer()
        self.assertEqual(trailer_text, "Воспроизведение трейлера фильма 'Movie1'")

        self.assertEqual(self.movie.get_media_type(), "movie")

    # 3. Тест полиморфного поведения
    def test_polymorphism(self):
        movie_desc = self.movie.get_description()

        book = Book.objects.create(
            title="1984",
            creator="George Orwell",
            publication_date=date(1949, 6, 8),
            isbn="12345",
            page_count=328
        )
        book_desc = book.get_description()

        audiobook = AudioBook.objects.create(
            title="Dune",
            creator="Frank Herbert",
            publication_date=date(2000, 1, 1),
            duration=600,
            narrator="John Doe"
        )
        audio_desc = audiobook.get_description()

        self.assertNotEqual(movie_desc, book_desc)
        self.assertNotEqual(movie_desc, audio_desc)
        self.assertNotEqual(book_desc, audio_desc)

    # 4. Тест использования миксинов
    def test_mixins_usage(self):
        self.assertTrue(hasattr(self.movie, "download"))
        self.assertTrue(callable(self.movie.download))

        audiobook = AudioBook.objects.create(
            title="Audiobook1",
            creator="ACreator1",
            publication_date=date(2025, 1, 1),
            duration=123,
            narrator="Narrator1"
        )

        self.assertTrue(hasattr(audiobook, "download"))
        self.assertTrue(hasattr(audiobook, "borrow"))
        self.assertTrue(callable(audiobook.borrow))
        self.assertTrue(callable(audiobook.download))
