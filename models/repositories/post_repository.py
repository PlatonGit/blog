from db import DbService
from models import Post


class PostRepository:
    __db = None

    def __init__(self, db: DbService):
        self.__db = db
        

    def create_post(self, post: Post):
        """
        Serves as a creator of posts in the database.
        :param post: - Post.
        :return bool: - False means error, True means successful creation.
        """
        try:
            with self.__db.connection.cursor() as cursor:  # ignore it
                query = "INSERT INTO post (user_id, title, text) VALUES ({user_id}, '{title}', '{text}')"
                query = query.format(
                    user_id = post.user_id,
                    title = post.title,
                    text = post.text
                )

                self.__db.execute(query)
            return True
        except Exception as ex:
            print(ex)
            return False

    