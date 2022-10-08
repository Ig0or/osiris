from decouple import config


class AuthService:
    __ACCESS_TOKEN = config("META_ACCESS_TOKEN")

    @classmethod
    async def validate_access_token(cls, token: str) -> bool:
        if token == cls.__ACCESS_TOKEN:
            return True

        return False