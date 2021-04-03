from db import DbService
from models import BlogUser, Profile, Post
from models.repositories import UserRepository, ProfileRepository, PostRepository
from models.controllers import UserController, ProfileController, PostController
from menu import StartMenu
from custom_exceptions import RepositoryError, UserExitException



def main():
   start_menu = StartMenu()
   mode = 'start'
   user = None

   while True:
      try:
         if mode == 'start':
            user = start_menu.start_logic()
            mode = 'registered'
         elif mode == 'registered':
            print(f'Welcome, {user}!')
            raise UserExitException()
      except UserExitException:
         print('\n\n=================================================\nExiting the programm.\nThank you for using this software and goodbye!')
         exit(0)
      

if __name__  == '__main__':
   try:
      main()
   except KeyboardInterrupt:
      print('\n\n=================================================\nForced programm shutdown.\nThank you for using this software and goodbye!')

      








# def main():   
#    db = DbService()
#    post_repo = PostRepository(db)
#    post_controller = PostController(post_repo)
   
#    try:
#       first_name = 'Jeremy'
#       second_name = 'Charles'
#       last_name = 'Clarkson'
#       age = 60
      
#       query = "SELECT id FROM profile WHERE first_name = '{first_name}' AND second_name = '{second_name}' AND last_name = '{last_name}' AND age = {age}"
#       query = query.format(
#          first_name = first_name,
#          second_name = second_name,
#          last_name = last_name,
#          age = age
#       )
#       if (profile := db.execute(query)) is not None:           
#          print(profile.)
#    except Exception as ex:
#       print(ex)


# if __name__  == '__main__':
#        main()





   # try:
   #    if (profile := profile_controller.read_profile(4)) is not None:
   #       print(profile.first_name)
   #    else:
   #       print('none')
      
   # except Exception as ex:
   #    print(ex)