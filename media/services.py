from media.models import Book, AudioBook, Movie


class MediaFactory:
    @staticmethod
    def create_media(media_type, **kwargs):
        creators = {
            'book': Book,
            'movie': Movie,
            'audiobook': AudioBook,
        }

        media_class = creators.get(media_type)
        if not media_class:
            raise ValueError(f"Неизвестный тип медиа: {media_type}")

        return media_class.objects.create(**kwargs)

    @staticmethod
    def get_all_media_types():
        return ['book', 'movie', 'audiobook']

    @staticmethod
    def get_media_class(media_type):
        creators = {
            'book': Book,
            'movie': Movie,
            'audiobook': AudioBook,
        }

        return creators.get(media_type)
