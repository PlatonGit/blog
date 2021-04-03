from db import DbService
from models import BlogUser
from models.repositories import UserRepository
from models.controllers import UserController


def main():   
   db = DbService()
   user_repo = UserRepository(db)
   user_controller = UserController(user_repo)

   if user_controller.read_user(3) is not None:
      print('Success')
   else:
      print('Failure')


if __name__  == '__main__':
   main()
