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


    def select_user(self, id):
        """
        Returns User's instance from database with corresponding id.
        :param id: - int.
        :return User: - successful select means that there is a record with corresponding id.
        :return None: - there is no record with that id. 
        """

        # try:
        #     with self.__db.connection.cursor() as cursor:
        #         query = "SELECT * FROM blog_user WHERE id = %d" % id
        #         self.__db.execute(query)

        #         if self.__db.cursor.rowcount == 1:
        #             return User.from_dict(self.__db.cursor.fetchone())
        #         else:
        #             return None
        
        # except Exception as ex:
        #     print(ex)

    
    