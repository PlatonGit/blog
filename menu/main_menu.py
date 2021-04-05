from menu.base_menu import BaseMenu, Option
from db.dbservice import DbService


class MainMenu(BaseMenu):
    menu_options = (
        Option('1', 'My profile', 'gomyprofile'),
        Option('2', 'My page', 'gomypage'),
        Option('3', 'Log out', 'logout'),
    )

    def __init__(self):
        super().__init__('Main Menu', self.menu_options)


    def main_menu_logic(self):
        # user = None
        
        while True:
            mode = self.user_id_input()

            if mode == 'gomyprofile':               
                print('\nNothing to see here (construction in progress)')
            elif mode == 'gomypage':
                print('\nNothing to see here (construction in progress)')
            elif mode == 'logout':
                return None