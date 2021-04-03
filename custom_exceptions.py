class RepositoryError(Exception):
    pass


class DatabaseError(Exception):
    pass


class UserExitException(KeyboardInterrupt):
    pass


class UserInputTextException(Exception):
    pass


class UserInputNumException(Exception):
    pass