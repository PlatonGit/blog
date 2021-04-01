from db import DbService
from models import BlogUser
from models.repositories import UserRepository
from models.controllers import UserController


def main():   
   db = DbService()
   user_repo = UserRepository(db)
   user_controller = UserController(user_repo)

   user = BlogUser('speed_is_power', 'hammondyouidiot', 3)
   
   if user_controller.create_user(user):
      print('Success')
   else:
      print('Failure')


if __name__  == '__main__':
   main()
