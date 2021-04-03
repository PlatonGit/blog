from db import DbService
from models import BlogUser
from custom_exceptions import RepositoryError


class UserRepository:
    __db = None

    def __init__(self, db: DbService):
        self.__db = db
        

    def create_user(self, user: BlogUser):
        """
        Serves as a creator of users in the database.
        :param user: - BlogUser.
        """
        
        try:
            query = "INSERT INTO blog_user (username, password, profile_id) VALUES ('{username}', '{password}', {profile_id})"
            query = query.format(
                username = user.username,
                password = user.password,
                profile_id = user.profile_id
            )
            self.__db.execute(query)

        except Exception as ex:
            print(ex)
            raise RepositoryError


    def select_user(self, id = None, username = None):
        """
        Returns User's instance from database with corresponding id.
        :param id: - int.
        :return User: - successful select means that there is a record with corresponding id.
        :raise RepositoryError: - error occured while working with database.
        """
        
        try:
            if id is not None and username is None:
                query = "SELECT * FROM blog_user WHERE id = %d" % id
            
            elif id is None and username is not None:
                query = f"SELECT * FROM blog_user WHERE username = '{username}'"
            else:
                raise RepositoryError
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                return BlogUser.from_dict(self.__db.cursor.fetchone())
            else:
                return None

        except Exception as ex:
            print(ex)
            raise RepositoryError


    def update_user(self, user: BlogUser):
        """
        Updates User's instance with corrsponding description and / or data.
        :param user: - BlogUser
        :raise RepositoryError: - error occured while working with database.
        """

        try:
            query = "UPDATE blog_user SET username = '{username}', password = '{password}', profile_id = {profile_id} WHERE id = {id}"
            query = query.format(
                id = user.id,
                username = user.username,
                password = user.password,
                profile_id = user.profile_id
            )
            self.__db.execute(query)

        except Exception as ex:
            print(ex)
            raise RepositoryError


    def delete_user(self, id):
        """
        Deletes User's instance from database with corresponding id.
        :param id: - int.
        :raise RepositoryError: - error occured while working with database.
        """
        
        try:
            query = "DELETE FROM blog_user WHERE id = %d" % id
            self.__db.execute(query)

        except Exception as ex:
            print(ex)
            raise RepositoryError



    
    