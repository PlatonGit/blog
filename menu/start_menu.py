from menu.base_menu import BaseMenu, Option
from custom_exceptions import UserExitException
from db.dbservice import DbService
from models import BlogUser, Profile
from models.repositories import UserRepository, ProfileRepository
from models.controllers import UserController, ProfileController


class StartMenu(BaseMenu):
    db = DbService()
    user_repo = UserRepository(db)
    user_controller = UserController(user_repo)
    profile_repo = ProfileRepository(db)
    profile_controller = ProfileController(profile_repo)
    
    menu_options = (
        Option('1', 'Log in', 'login'),
        Option('2', 'Register', 'register'),
        Option('3', 'Exit', 'exit')
    )

    def __init__(self):
        super().__init__('Start Menu', self.menu_options)

    
    def login(self):
        login_attempts = 3

        while True:
            username = self.user_text_input('Enter your username (# to cancel): ')
            if username != '#':    
                user = self.user_controller.read_user(username = username)              
            else:
                return None
            
            if user is None:
                print(f'User with username \'{username}\' does not exist; are you sure you\'re entering a correct username?')
            else:
                while login_attempts >= 0:
                    password = self.user_text_input('Enter your password (# to cancel): ')
                    if password != '#':
                        if password == user.password:
                            return  user.username
                        else:
                            print(f'\nWrong password; attempts left - {login_attempts}.')
                            login_attempts -= 1
                    else:
                        return None             
                return None


    def register(self):
        while True:
            username = self.user_text_input('Enter your username (# to cancel): ')
            if username != '#':    
                if self.user_controller.read_user(username = username) is not None:
                    print(f'User with username \'{username}\' already exists; try a different username.')
                else:
                    break
            else:
                return None
        
        password = self.user_text_input('Enter your password: ')

        first_name = self.user_text_input('Enter your first name: ')
        second_name = self.user_text_input('Enter your second name: ')
        last_name = self.user_text_input('Enter your last name: ')
        age = self.user_num_input('Enter your age: ')
        
        if self.user_text_input('Press any key to confirm (# to cancel): ') != '#':
            profile = Profile(first_name, second_name, last_name, age)
            self.profile_controller.create_profile(profile)
            profile_id = self.profile_controller.read_profile(profile = profile).id

            user = BlogUser(username, password, profile_id)
            self.user_controller.create_user(user)
        else:
            return None

        return username

            
        
    def start_logic(self):
        user = None
        
        while True:
            mode = self.user_id_input()

            if mode == 'login':
                user = self.login()
                if user is not None:
                    return user

            elif mode == 'register':
                user = self.register()
                if user is not None:
                    return user

            elif mode == 'exit':
                raise UserExitException()
