from models.repositories import ProfileRepository


class ProfileController:
    __profile_repo = None

    def __init__(self, profile_repo: ProfileRepository):
        self.__profile_repo = profile_repo

    
    def create_profile(self, profile):
        return self.__profile_repo.create_profile(profile)

    
    def read_profile(self):
        pass


    def update_profile(self):
        pass


    def delete_profile(self):
        pass