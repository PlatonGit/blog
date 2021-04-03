from models.repositories import ProfileRepository


class ProfileController:
    __profile_repo = None

    def __init__(self, profile_repo: ProfileRepository):
        self.__profile_repo = profile_repo

    
    def create_profile(self, profile):
        return self.__profile_repo.create_profile(profile)

    
    def read_profile(self, id = None, profile = None):
        return self.__profile_repo.select_profile(id, profile)


    def update_profile(self, profile):
        return self.__profile_repo.update_profile(profile)


    def delete_profile(self, id):
        return self.__profile_repo.delete_profile(id)