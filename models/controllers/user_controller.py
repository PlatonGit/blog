from models.repositories import UserRepository


class UserController:
    __user_repo = None

    def __init__(self, user_repo: UserRepository):
        self.__user_repo = user_repo


    def create_user(self, user):
        return self.__user_repo.create_user(user)


    def read_user(self, id):
        return self.__user_repo.select_user(id)


    def update_user(self):
        pass


    def delete_user(self):
        pass