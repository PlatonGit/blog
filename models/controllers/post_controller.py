from models.repositories import PostRepository


class PostController:
    __post_repo = None

    def __init__(self, post_repo: PostRepository):
        self.__post_repo = post_repo


    def create_post(self, post):
        return self.__post_repo.create_post(post)


    def read_post(self):
        pass


    def update_post(self):
        pass


    def delete_post(self):
        pass