from db import DbService
from models import Profile


class ProfileRepository:
    __db = None

    def __init__(self, db: DbService):
        self.__db = db

    
    def create_profile(self, profile: Profile):
        """
        Serves as a creator of profiles in the database.
        :param profile: - Profile.
        :return bool: - False means error, True means successful creation.
        """
        try:
            with self.__db.connection.cursor() as cursor:  # ignore it
                query = "INSERT INTO profile (first_name, second_name, last_name, age) VALUES ('{first_name}', '{second_name}', '{last_name}', {age})"
                query = query.format(
                    first_name = profile.first_name,
                    second_name = profile.second_name,
                    last_name = profile.last_name,
                    age = profile.age
                )

                self.__db.execute(query)
            return True
        except Exception as ex:
            print(ex)
            return False