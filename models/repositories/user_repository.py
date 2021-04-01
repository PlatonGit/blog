from db import DbService
from models import BlogUser


class UserRepository:
    __db = None

    def __init__(self, db: DbService):
        self.__db = db
        

    def create_user(self, user: BlogUser):
        """
        Serves as a creator of users in the database.
        :param user: - User.
        :return bool: - False means error, True means successful creation.
        """
        try:
            with self.__db.connection.cursor() as cursor:  # ignore it
                query = "INSERT INTO blog_user (username, password, profile_id) VALUES ('{username}', '{password}', {profile_id})"
                query = query.format(
                    username = user.username,
                    password = user.password,
                    profile_id = user.profile_id
                )

                self.__db.execute(query)
            return True
        except Exception as ex:
            print(ex)
            return False