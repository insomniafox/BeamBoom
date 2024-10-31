def dir_for_user(user: "User", filename: str) -> str:
    """
        Получить директорию для сохранения аватарок
    """
    return '/'.join(['users', user.phone, filename])
